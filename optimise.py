import os
import glob
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageOps
import webbrowser
import threading

class ImageResizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Optimise by Oashim Akram")
        self.root.geometry("460x690")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.folder_path = tk.StringVar(value=os.getcwd())
        self.prefix = tk.StringVar(value="photo")
        self.width = tk.IntVar(value=800)
        self.height = tk.IntVar(value=600)
        self.quality = tk.IntVar(value=85)
        self.method = tk.IntVar(value=1)
        self.bg_color = tk.StringVar(value="black")
        
        self.setup_ui()
    
    def setup_ui(self):

        # Main container with scrollbar
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Folder Selection
        folder_frame = self.create_section(main_frame, "📁 Folder Selection")
        
        tk.Button(folder_frame, text="Choose Folder", 
                 command=self.select_folder,
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
                 relief='flat', padx=20, pady=8).pack(side='left', padx=(0,10))
        
        folder_label = tk.Label(folder_frame, textvariable=self.folder_path,
                               bg='#ecf0f1', fg='#2c3e50', font=('Arial', 9),
                               relief='sunken', padx=10, pady=5)
        folder_label.pack(fill='x', expand=True)
        
        # Settings Section
        settings_frame = self.create_section(main_frame, "⚙️ Resize Settings")
        
        # Prefix
        prefix_row = tk.Frame(settings_frame, bg='#34495e')
        prefix_row.pack(fill='x', pady=5)
        tk.Label(prefix_row, text="File Prefix:", 
                bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(side='left')
        prefix_entry = tk.Entry(prefix_row, textvariable=self.prefix, 
                               font=('Arial', 10), width=15)
        prefix_entry.pack(side='right')
        
        # Dimensions
        dim_row = tk.Frame(settings_frame, bg='#34495e')
        dim_row.pack(fill='x', pady=5)
        tk.Label(dim_row, text="Dimensions (W×H):", 
                bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(side='left')
        
        dim_controls = tk.Frame(dim_row, bg='#34495e')
        dim_controls.pack(side='right')
        tk.Entry(dim_controls, textvariable=self.width, font=('Arial', 10), width=8).pack(side='left')
        tk.Label(dim_controls, text=" × ", bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(side='left')
        tk.Entry(dim_controls, textvariable=self.height, font=('Arial', 10), width=8).pack(side='left')
        
        # Quality
        quality_row = tk.Frame(settings_frame, bg='#34495e')
        quality_row.pack(fill='x', pady=5)
        tk.Label(quality_row, text="JPEG Quality:", 
                bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(side='left')
        
        quality_frame = tk.Frame(quality_row, bg='#34495e')
        quality_frame.pack(side='right')
        quality_scale = tk.Scale(quality_frame, from_=10, to=100, orient='horizontal',
                                variable=self.quality, bg='#34495e', fg='white',
                                highlightthickness=0, length=200)
        quality_scale.pack(side='left')
        quality_label = tk.Label(quality_frame, textvariable=self.quality,
                               bg='#34495e', fg='white', font=('Arial', 10, 'bold'),
                               width=3)
        quality_label.pack(side='left', padx=(10,0))
        
        # Method Selection
        method_frame = self.create_section(main_frame, "🎯 Resize Method")
        
        methods = [
            ("Fill and Crop | outfit cover", 1, "Crops to exact ratio, no padding"),
            ("Force Stretch", 2, "May distort image"),
            ("Fit with Padding", 3, "Keeps aspect ratio, adds background")
        ]
        
        for text, value, desc in methods:
            method_row = tk.Frame(method_frame, bg='#34495e')
            method_row.pack(fill='x', pady=2)
            
            tk.Radiobutton(method_row, text=text, variable=self.method, value=value,
                          bg='#34495e', fg='white', selectcolor='#2c3e50',
                          font=('Arial', 10, 'bold')).pack(side='left')
            
            tk.Label(method_row, text=f"({desc})", 
                    bg='#34495e', fg='#bdc3c7', font=('Arial', 8)).pack(side='left', padx=(10,0))
        
        # Background Color (only for method 3)
        bg_frame = tk.Frame(method_frame, bg='#34495e')
        bg_frame.pack(fill='x', pady=5)
        tk.Label(bg_frame, text="Background Color:", 
                bg='#34495e', fg='white', font=('Arial', 10, 'bold')).pack(side='left')
        
        bg_combo = ttk.Combobox(bg_frame, textvariable=self.bg_color,
                               values=['black', 'white', 'red', 'blue', 'green'],
                               width=10, state='readonly')
        bg_combo.pack(side='right')
        
        # Process Button
        process_frame = tk.Frame(main_frame, bg='#2c3e50')
        process_frame.pack(fill='x', pady=20)
        
        self.process_btn = tk.Button(process_frame, text="🚀 Start Processing", 
                                    command=self.start_processing,
                                    bg="#43ea34", fg='white', font=('Arial', 12, 'bold'),
                                    relief='flat', padx=30, pady=12)
        self.process_btn.pack(expand=True)
        
        #developed by oashim akram
        footer_frame = tk.Frame(main_frame, bg='#2c3e50')
        footer_frame.pack(fill='x', pady=(10,0))

        credit_static = tk.Label(footer_frame, text="Developed by ",
                     bg='#2c3e50', fg='#ecf0f1', font=('Arial', 9))
        credit_static.pack(side='left', padx=(10,0))

        name_label = tk.Label(footer_frame, text="Oashim Akram",
                      fg='#3498db', bg='#2c3e50', cursor='hand2',
                      font=('Arial', 9, 'underline'))
        name_label.pack(side='left', padx=(0,8))

        def _open_dev_link(event=None):
            try:
                webbrowser.open_new("https://www.facebook.com/devOashim")
            except Exception:
                pass

        name_label.bind("<Button-1>", _open_dev_link)

        # Progress Section (created hidden; shown only while processing)
        progress_content = self.create_section(main_frame, "📊 Progress")
        progress_section = progress_content.master  # outer section_frame created by create_section

        self.progress_var = tk.StringVar(value="Ready to process images")
        self.progress_label = tk.Label(progress_content, textvariable=self.progress_var,
                          bg='#34495e', fg='white', font=('Arial', 10))
        self.progress_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(progress_content, length=400, mode='determinate')
        self.progress_bar.pack(pady=5)

        # Results area (in its own frame so we can hide/show easily)
        self.results_frame = tk.Frame(main_frame, bg='#ecf0f1')
        self.results_text = tk.Text(self.results_frame, height=8, bg='#ecf0f1', fg='#2c3e50',
                        font=('Consolas', 9))
        self.results_text.pack(fill='both', expand=True, side='left', pady=(10,0))

        scrollbar = tk.Scrollbar(self.results_frame)
        scrollbar.pack(side='right', fill='y')
        self.results_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_text.yview)

        # Initially hide progress/results UI
        progress_section.pack_forget()
        self.results_frame.pack_forget()

        # Helper methods to show/hide progress areas
        def _show_progress():
            # show progress section and results
            try:
                progress_section.pack(fill='x', pady=10, padx=10)
            except Exception:
                pass
            try:
                self.results_frame.pack(fill='both', expand=True, pady=(10,0))
            except Exception:
                pass

        def _hide_progress():
            try:
                progress_section.pack_forget()
            except Exception:
                pass
            try:
                self.results_frame.pack_forget()
            except Exception:
                pass

        # attach to self so other methods can use them if needed
        self.show_progress = _show_progress
        self.hide_progress = _hide_progress

        # Wrap the existing start_processing command so UI shows progress only during run
        original_start = getattr(self, "start_processing", None)
        if original_start:
            def _wrapped_start():
                self.show_progress()
                original_start()

                # Poll for completion (start_processing spawns a thread and will re-enable button when done)
                def _poll_done():
                    if self.process_btn['state'] == 'normal':
                        # finished
                        self.hide_progress()
                    else:
                        self.root.after(500, _poll_done)
                self.root.after(500, _poll_done)

            # Rebind process button to wrapped starter
            try:
                self.process_btn.config(command=_wrapped_start)
            except Exception:
                pass
    
    def create_section(self, parent, title):
        section_frame = tk.Frame(parent, bg='#34495e', relief='raised', bd=1)
        section_frame.pack(fill='x', pady=10, padx=10)
        
        title_label = tk.Label(section_frame, text=title, 
                              font=('Arial', 12, 'bold'), 
                              fg='#ecf0f1', bg='#34495e')
        title_label.pack(anchor='w', padx=10, pady=(10,5))
        
        content_frame = tk.Frame(section_frame, bg='#34495e')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        return content_frame
    
    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Image Folder")
        if folder:
            self.folder_path.set(folder)
    
    def log_message(self, message):
        self.results_text.insert('end', message + '\n')
        self.results_text.see('end')
        self.root.update_idletasks()
    
    def resize_image_method1(self, img, target_width, target_height, bg_color):
        """Fit with padding (keeps aspect ratio, adds background)"""
        img_ratio = img.width / img.height
        target_ratio = target_width / target_height
        
        if img_ratio > target_ratio:
            new_width = target_width
            new_height = int(target_width / img_ratio)
        else:
            new_height = target_height
            new_width = int(target_height * img_ratio)
        
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        new_img = Image.new('RGB', (target_width, target_height), bg_color)
        
        paste_x = (target_width - new_width) // 2
        paste_y = (target_height - new_height) // 2
        new_img.paste(resized_img, (paste_x, paste_y))
        
        return new_img
    
    def resize_image_method2(self, img, target_width, target_height):
        """Fill and crop (crops to exact ratio, no padding) - Laravel cover() equivalent"""
        img_ratio = img.width / img.height
        target_ratio = target_width / target_height
        
        if img_ratio > target_ratio:
            new_height = target_height
            new_width = int(target_height * img_ratio)
        else:
            new_width = target_width
            new_height = int(target_width / img_ratio)
        
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        left = (new_width - target_width) // 2
        top = (new_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height
        
        cropped_img = resized_img.crop((left, top, right, bottom))
        return cropped_img
    
    def resize_image_method3(self, img, target_width, target_height):
        """Force stretch (may distort image)"""
        return img.resize((target_width, target_height), Image.LANCZOS)
    
    def process_images(self):
        try:
            current_dir = self.folder_path.get()
            prefix = self.prefix.get()
            width = self.width.get()
            height = self.height.get()
            quality = self.quality.get()
            method = self.method.get()
            bg_color = self.bg_color.get()
            
            # Clear results
            self.results_text.delete(1.0, 'end')
            
            # Create output folder
            output_folder = os.path.join(current_dir, f"{prefix}s")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Find images
            extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff']
            image_files = []
            for ext in extensions:
                image_files.extend(glob.glob(os.path.join(current_dir, ext)))
            
            if not image_files:
                messagebox.showwarning("No Images", "No image files found in selected folder!")
                return
            
            total_files = len(image_files)
            self.progress_bar.config(maximum=total_files)
            
            self.log_message(f"Found {total_files} images. Starting processing...")
            self.log_message(f"Target size: {width}x{height}, Quality: {quality}%")
            self.log_message("-" * 60)
            
            counter = 1
            for i, file_path in enumerate(image_files):
                filename = os.path.basename(file_path)
                self.progress_var.set(f"Processing {filename}... ({i+1}/{total_files})")
                
                try:
                    img = Image.open(file_path)
                    
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Apply selected method
                    if method == 1:
                        processed_img = self.resize_image_method2(img, width, height)
                    elif method == 2:
                        processed_img = self.resize_image_method3(img, width, height)
                    else:
                        processed_img = self.resize_image_method1(img, width, height, bg_color)
                    
                    # Save processed image
                    output_path = os.path.join(output_folder, f"{prefix}-{counter}.jpg")
                    
                    processed_img.save(output_path, 'JPEG', 
                                     quality=quality,
                                     optimize=True,
                                     progressive=True)
                    
                    # Log results
                    original_size = os.path.getsize(file_path)
                    new_size = os.path.getsize(output_path)
                    size_reduction = ((original_size - new_size) / original_size) * 100
                    
                    self.log_message(f"✓ {filename}")
                    self.log_message(f"  {original_size/1024:.1f}KB → {new_size/1024:.1f}KB ({size_reduction:+.1f}%)")
                    
                    counter += 1
                    img.close()
                    processed_img.close()
                    
                except Exception as e:
                    self.log_message(f"✗ Error processing {filename}: {str(e)}")
                
                self.progress_bar['value'] = i + 1
                self.root.update_idletasks()
            
            self.progress_var.set(f"✅ Completed! Processed {counter-1} images")
            self.log_message("-" * 60)
            self.log_message(f"🎉 All done! Images saved in: {output_folder}")
            messagebox.showinfo("Success", f"Successfully processed {counter-1} images!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        finally:
            self.process_btn.config(state='normal', text="🚀 Start Processing")
    
    def start_processing(self):
        self.process_btn.config(state='disabled', text="⏳ Processing...")
        # Run in separate thread to prevent UI freezing
        thread = threading.Thread(target=self.process_images)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerGUI(root)
    root.mainloop()