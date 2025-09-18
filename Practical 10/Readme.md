# Motion Tracking with Blender

This folder contains the files and documentation for **Visual Effects & Computer Graphics Practical – Motion Tracking with Blender**.

## 🎯 Objective
To learn and demonstrate 3D camera tracking (match moving) using Blender by importing real-world footage, tracking camera movement, and compositing 3D elements into the scene.

## 📝 Description
This project shows how to:
- Import real-world footage into Blender.
- Track multiple feature points across frames.
- Solve the camera motion.
- Set the scene scale and orientation.
- Place a 3D object into the tracked scene.
- Render the final composite as an MP4 video.

## 🛠️ Tools & Software
- **Blender** (v3.x or later)
- Free test footage (.mp4) 

## 📂 Repository Contents
- `Motion Tracking.blend` – Blender project files (`.blend`).
- `Input Video` – Original footage used for tracking (`.mp4`).
- `Output Render.mp4` – Final rendered video(s).
- `README.md` – This file.

## 🚀 How to Reproduce
1. Clone this repository.
2. Open the `.blend` file in Blender.
3. Switch to the **Motion Tracking** workspace.
4. Load the footage (`footage/video.mp4`).
5. Detect & track features (minimum 8 stable tracks).
6. Solve the camera motion.
7. Add a 3D object to the scene.
8. Set **Output Properties → File Format = FFmpeg Video**, **Container = MPEG-4**, **Codec = H.264**.
9. Render the animation (`Ctrl+F12`) to produce the final MP4.
