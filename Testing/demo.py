import cv2

# Load images to be stitched
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

# Create a Stitcher object
stitcher = cv2.Stitcher_create()

# Perform stitching
status, stitched_image = stitcher.stitch([image1, image2])

# Check if stitching was successful
if status == cv2.Stitcher_OK:
    # Show the stitched image
    cv2.imshow("Stitched Panorama", stitched_image)

    # Save the stitched image
    cv2.imwrite("stitched_output.jpg", stitched_image)
    print("Panoramic image saved as 'stitched_output.jpg'.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error during stitching, code:", status)
