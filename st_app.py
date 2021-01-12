''' This app has been tested on Ubuntu20, CUDA10.1, driver 460, GTX 980, Pascal VOC Model'''

import streamlit as st
import pixellib
from pixellib.semantic import semantic_segmentation

def pascal_voc_overlay(the_image):
    segment_image = semantic_segmentation()
    segment_image.load_pascalvoc_model("model/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    segment_image.segmentAsPascalvoc(
        the_image, 
    output_image_name = 'res'+'/'+f'{the_image}',
    overlay=True)
    st.image(f'res/{the_image}', caption='Output Image')

st.title('Image Segmentation')
st.header('Segmentation using Pascal VOC model')

up_img = st.file_uploader('Upload image:', type=['jpg', 'jpeg', 'png'])
if up_img:
    st.image(up_img, caption='Input Image')
    pascal_voc_overlay(up_img)
else:
    st.write('Please upload your image...')

st.subheader('This has been prepared by: Cyborg009, Seramamas')