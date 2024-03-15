import streamlit as st
import cv2
from PIL import Image
import numpy as np

def smooth_image(image, kernel_size=5):
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return smoothed_image

def sketch_image(image):
    # Convertendo a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicando o filtro de inversão
    inverted_gray_image = cv2.bitwise_not(gray_image)
    # Aplicando a transformação de desfoque gaussiano
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), sigmaX=0, sigmaY=0)
    # Realizando a operação de esboço
    inverted_blurred_image = 255 - blurred_image
    # Misturando a imagem original com o esboço
    sketched_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return sketched_image

def main():
    st.title("Aplicativo de Suavização e Esboço de Imagens")
    st.write("Este aplicativo permite suavizar uma imagem utilizando a operação de borramento (smoothing) ou convertê-la em um esboço.")
    
    uploaded_image = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
    sketch_option = st.checkbox("Converter em esboço")
    
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Imagem Original", use_column_width=True)
        
        # Converte a imagem para array numpy
        img_array = np.array(image)
        
        # Botão para suavizar a imagem
        if st.button("Processar"):
            if sketch_option:
                processed_img = sketch_image(img_array)
                st.image(processed_img, caption="Imagem Processada", use_column_width=True)
            else:
                smoothed_img = smooth_image(img_array)
                st.image(smoothed_img, caption="Imagem Suavizada", use_column_width=True)
            
if __name__ == "__main__":
    main()
