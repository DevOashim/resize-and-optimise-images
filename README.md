# 🖼️ Image Optimiser (GUI + CLI Versions)

A powerful yet simple **Image Resize & Optimiser Tool** built with **Python + Pillow**.  
It includes both a **GUI (Tkinter)** version and a **CLI (optimise.exe)** version.

---

## ✨ Features

### ✅ GUI Version (Tkinter)
- 📂 Select any folder with images (`jpg, jpeg, png, bmp, tiff`)
- 📛 Custom file prefix for processed images
- 📐 Set target **Width × Height**
- 🎯 Resize methods:
  - **Fill & Crop** (cover style, no padding)
  - **Force Stretch** (distorts to fit)
  - **Fit with Padding** (keeps aspect ratio, background fill)
- 🎨 Custom background color (for padding method)
- 📉 Adjustable **JPEG quality slider** (10–100)
- ⚡ Optimises output images (`optimize=True`, `progressive=True`)
- 📊 Real-time progress bar and logs
- ✅ Shows original size vs new size + percentage reduction
- 🪟 User-friendly dark themed GUI

### ✅ CLI Version (optimise.exe)
- 📂 Works in the **current folder** (where CMD is opened)
- 🔄 Resize methods:
  1. Fill and Crop (cover style, no padding)
  2. Force Stretch (may distort)
  3. Fit with Padding (keeps aspect ratio, background color)
- 🎨 Custom background color support
- 🖼️ Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`
- 💾 Auto saves in new folder with prefix name
- ⚡ Lightweight `.exe`, no Python required
- 🚀 Works globally from any folder

---

## 🚀 Installation

### 🔹 For GUI (Python script)
1. Clone the repository:
   ```bash
   git clone https://github.com/DevOashim/resize-and-optimise-images
   cd resize-and-optimise-images
   ```
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Run the GUI:
   ```bash
   python optimise.py
   ```

### 🔹 For CLI (optimise.exe)
1. Download `optimise.exe` from [Releases](https://github.com/DevOashim/resize-and-optimise-images/releases).  
2. Copy `optimise.exe` into:
   ```
   C:\Windows
   ```
3. Now you can run from any folder:
   ```bash
   optimise
   ```

---

## 📂 Output

Processed images are saved in a new folder named after your prefix.  
File names are auto-numbered, e.g.:

```
photo-1.jpg
photo-2.jpg
photo-3.jpg
```

---

## 📊 Example (CLI)

```bash
optimise
```

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

**Output folder → `myimgs/` containing:**
```
myimg-1.jpg
myimg-2.jpg
```

---

## 🖼️ Example (GUI)
- Input: `E:\MyPictures`
- Settings: Width `800`, Height `600`, Quality `85`, Method `Fit with Padding`
- Output: `E:\MyPictures\photos\`

---

## 📜 License
MIT License – Free to use, modify, and distribute.

---

## 👨‍💻 Author
Built with ❤️ by [@DevOasbim](https://github.com/DevOashim)
