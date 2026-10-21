# riichi-maker.html（Claude アーティファクト版）から、GitHub Pages 用の単体 index.html を作る
import pathlib
src = pathlib.Path(__file__).with_name('riichi-maker.html').read_text(encoding='utf-8')
head, body = src.split('</style>\n', 1)
head += '</style>\n'
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = head.replace('<style>\n', '<style>\n*, *::before, *::after { box-sizing: border-box; }\nbody { margin: 0; }\nimg { max-width: 100%; }\n', 1)
old = """  if (!downloads) { msg('この表示では直接保存できません。動画を右クリック（長押し）して保存してください。', true); return; }"""
new = """  if (!downloads) {
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = filename;
    document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    msg(`${filename} をダウンロードしました。`); return;
  }"""
assert old in body
body = body.replace(old, new)
out = ('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="キャラ画像を入れて背景と効果音を選ぶだけで、麻雀のリーチ演出を作って動画で書き出せるツール。">\n'
       + head + '</head>\n<body>\n' + body + '</body>\n</html>\n')
pathlib.Path(__file__).with_name('docs').joinpath('index.html').write_text(out, encoding='utf-8')
print('ok', len(out))
