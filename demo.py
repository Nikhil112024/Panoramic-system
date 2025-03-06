import cv2
import numpy as np

# Load video frames from multiple cameras
frame1 = cv2.imread("camera1_frame.jpg")
frame2 = cv2.imread("camera2_frame.jpg")

# Convert to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# Feature detection
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Feature matching
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply Lowe’s ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Extract matched keypoints
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Compute homography
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Warp images
stitched_frame = cv2.warpPerspective(frame1, H, (frame1.shape[1] + frame2.shape[1], frame1.shape[0]))
stitched_frame[0:frame2.shape[0], 0:frame2.shape[1]] = frame2

# Show result
cv2.imshow("Panoramic Video", stitched_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

