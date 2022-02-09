# cryptoapes-skin-selector

This project is here bacause someone wants the codes, you need know it well.

## script
### auto_generate_wallpaper.py

sample: https://crapes.redenvelop.app/cryptoapes/Solavirus_Wallpaper/1.png 

generating Solavirus Wallpaper based on crape's trait, because there are 8 color backgrouds and you need match crape pfp color with wallpaper colors

### auto_generate.py
sample: https://crapes.redenvelop.app/cryptoapes/StaryNight_VanGogh/1.gif
generating gif background memes. You need pre-generate background cut-off PNG first.

After generating all meme gif or png, you need upload to server and provide http access.

## Website
Website provide UI for user to choose their crape number and type of meme they want to preview. Website load the URL generated above based on user's input.

You need edit on your own situation.

### Development
```bash
npm install
npm run dev
```

visit src/index.html

### Distribution

```bash
npm install

# in macOS, the GNU sed is required
brew install gsed
npm run build:mac

# in Linux
brew install gsed
npm run build:linux
```

Then copy `dist` to anywhere.
