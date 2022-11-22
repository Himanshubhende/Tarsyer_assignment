import cv2
import common

rectangle_points = []

def draw_rectangle_and_label(img, label):
    crop_cor = img[rectangle_points[0][1]:rectangle_points[1][1], rectangle_points[0][0]:rectangle_points[1][0]]
    cv2.imwrite('Task_1_cropped.jpg',crop_cor)

    label1=str(rectangle_points[0][1])+' '+str(rectangle_points[1][1]) 
    label2=str(rectangle_points[0][0])+' '+str(rectangle_points[1][0]) 
    text_origin = (rectangle_points[0][0], rectangle_points[0][1] - common.TEXT_OFFSET)
    text_end = (rectangle_points[1][0], rectangle_points[1][1] - common.TEXT_OFFSET)

    cv2.rectangle(img, rectangle_points[0], rectangle_points[1], common.GREEN, common.LINE_THICKNESS)
    
    
    cv2.putText(img, label1, text_origin, common.FONT_FACE, common.FONT_SCALE, common.GREEN, common.FONT_THICKNESS, common.FONT_LINE)
    cv2.putText(img, label2, text_end, common.FONT_FACE, common.FONT_SCALE, common.GREEN, common.FONT_THICKNESS, common.FONT_LINE)
    
    cv2.imwrite('Task_1_insights.jpg',img)

def display_lena_image(draw_rectangle):
    # File path
    file_path = common.LENA_FILE_PATH

    # Load image
    lena_img = cv2.imread(file_path)

    # Draw rectangle
    if(draw_rectangle):
        draw_rectangle_and_label(lena_img, 'Lena')

    # Show image
    cv2.imshow(common.WINDOW_NAME, lena_img)
    cv2.waitKey(0)
    
def on_mouse_move(event, x, y, flags, param):
    # User pressed left mouse button and started drawing the rectangle    
    if(event == cv2.EVENT_LBUTTONDOWN):   
        rectangle_points.clear()
        rectangle_points.append((x,y))                 
    
    # User has finished drawing the rectangle
    elif event == cv2.EVENT_LBUTTONUP:
        rectangle_points.append((x,y))
        display_lena_image(True)        

# Prepare window and set mouse callback
cv2.namedWindow(common.WINDOW_NAME)
cv2.setMouseCallback(common.WINDOW_NAME, on_mouse_move)

# Display Lena image
display_lena_image(False)