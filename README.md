# Panoramic Video System

## Overview
The **Panoramic Video System** integrates multiple CCTV camera feeds to generate a seamless panoramic view in real-time. This technique enhances situational awareness by providing a unified perspective of the monitored area.

---

## 📌 How It Works

### 1. **Camera Calibration**
To correctly align multiple camera feeds, intrinsic and extrinsic camera parameters are estimated:
- **Intrinsic Calibration**: Determines camera-specific parameters like focal length, optical center, and distortion coefficients.
- **Extrinsic Calibration**: Establishes spatial relationships between cameras by finding rotation and translation matrices.

Tools: **OpenCV’s `cv2.calibrateCamera()` and `cv2.findHomography()`**

---

### 2. **Feature Detection & Matching**
- Key features are detected in overlapping regions of adjacent video feeds using feature detection algorithms like:
  - **SIFT (Scale-Invariant Feature Transform)**
  - **ORB (Oriented FAST and Rotated BRIEF)**
- Matching features between adjacent frames is performed using:
  - **FLANN (Fast Library for Approximate Nearest Neighbors)**
  - **BFMatcher (Brute-Force Matcher)**

Tools: **OpenCV’s `cv2.SIFT_create()` and `cv2.BFMatcher()`**

---
Work in Progress..
### 3. **Homography Estimation**
- A **homography matrix** is computed to transform points from one camera’s view to another.
- This is done using **RANSAC (Random Sample Consensus)** to filter out incorrect matches and improve alignment.

Formula:
