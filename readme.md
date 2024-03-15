# Aplicativo de Suavização e Esboço de Imagens

Este é um aplicativo simples desenvolvido com Streamlit, uma biblioteca Python para criação de aplicativos web interativos. O aplicativo permite carregar uma imagem, suavizá-la utilizando a operação de borramento (smoothing) ou convertê-la em um esboço, e exibir o resultado ao usuário.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/).

2. Clone este repositório ou faça o download do arquivo [index.py](index.py).

3. No terminal, navegue até o diretório do projeto e instale as dependências executando o seguinte comando:
    ```
    pip install streamlit opencv-python
    ```

## Como usar

1. No terminal, navegue até o diretório do projeto.

2. Execute o aplicativo Streamlit executando o seguinte comando:
    ```
    streamlit run index.py
    ```

3. O aplicativo será aberto automaticamente em seu navegador padrão.

4. Você pode carregar uma imagem clicando no botão "Escolha uma imagem".

5. Selecione a opção "Converter em esboço" se desejar que a imagem final seja apresentada como um esboço.

6. Clique no botão "Processar" para aplicar a operação selecionada à imagem.

7. A imagem resultante será exibida no aplicativo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos. Para sugestões ou problemas encontrados, por favor, abra uma issue.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
