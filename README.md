# 🖼️ Optimise.exe - Image Resizer Tool

A simple **Windows CLI tool** built with Python & PyInstaller that helps you **resize and optimise images** directly from the command line.  
You can run it in **any folder** without moving images anywhere.

---

## ✨ Features

- 📂 Works in the **current folder** (where CMD is opened).
- 🔄 Supports multiple resize methods:
  1. **Fill and Crop** – crops to exact ratio, no padding (like CSS `cover()`).
  2. **Force Stretch** – resizes to exact size (may distort).
  3. **Fit with Padding** – keeps aspect ratio and adds background color.
- 🎨 Supports custom background color (black/white/red/blue).
- 🖼️ Supported image formats:  
  `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`
- 💾 Auto saves processed images in a new folder with prefix name.
- ⚡ Lightweight `.exe`, no external dependencies required.
- 🚀 Works from **anywhere** after installation.

---

## 📥 Installation

1. Download `optimise.exe` from [Releases](https://github.com/DevOashim/resize-and-optimise-images/blob/main/optimise.exe).  
2. Copy `optimise.exe` into:

   ```
   C:\Windows
   ```

3. Done ✅ Now you can run the tool with:

```bash
optimise
```

from **any folder, any user**.

---

## 🖥️ Usage

1. Open **CMD** in the folder containing images.
2. Run:

```bash
optimise
```

3. Follow interactive prompts:
   - Enter file prefix name (e.g., `photo`)
   - Enter target width (px)
   - Enter target height (px)
   - Choose resize method (1, 2, or 3)
   - If padding method → choose background color

---

## 📊 Example

**Command:**
```bash
optimise
```

**Input during run:**
```
Enter file prefix name (example: photo): myimg
Enter target width (px): 800
Enter target height (px): 600

Choose resize method:
1. Fill and crop (crops to exact ratio, no padding)
2. Force stretch (may distort image)
3. Fit with padding (keeps aspect ratio, adds background)
Enter method (1, 2, or 3): 3
Enter background color (black/white/red/blue, default: black): white
```

**Output:**
```
Processing image1.jpg...
Processing image2.png...
Done! Images saved in folder 'myimgs'
```

Result → `myimgs/` folder will contain:
```
myimg-1.jpg
myimg-2.jpg
```

---

## ⚖️ License

MIT License – free to use and modify.

---

## 👨‍💻 Author

Built with ❤️ by [@DevOasbim](https://github.com/DevOashim)
