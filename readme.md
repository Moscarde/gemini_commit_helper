# Gerador de Mensagens de Commit

Este é um script Python que ajuda você a gerar mensagens de commit padronizadas seguindo a especificação **Conventional Commits**. Ele usa a API do Gemini para analisar a entrada do usuário (uma descrição breve ou um trecho de código) e gera uma mensagem de commit no formato correto.

## Funcionalidades

- **Conventional Commits**: Gera mensagens de commit seguindo a especificação [Conventional Commits](https://www.conventionalcommits.org/).
    
- **Fácil de Usar**: Aceita tanto descrições breves quanto trechos de código como entrada.
    
- **Integração com Área de Transferência**: Copia automaticamente a mensagem de commit gerada para a área de transferência.
    
- **Multiplataforma**: Funciona tanto no Windows quanto no Linux.
    

---

## Pré-requisitos

Antes de executar o script, certifique-se de ter o seguinte instalado:

1. **Python 3.x**: Baixe e instale o Python a partir de [python.org](https://www.python.org/).
    
2. **Bibliotecas Necessárias**: Instale as bibliotecas Python necessárias usando o pip:

```bash
    pip install requests pyperclip
``` 
3. **Chave da API Gemini**: Obtenha uma chave de API do Gemini e substitua `YOUR_API_KEY_HERE` no script ou importe de um .env.
    

---

## Como Usar

1. **Clone o Repositório**:

```bash    
    git clone https://github.com/Moscarde/gemini_commit_helper.git
    cd gemini_commit_helper
```    

2. **Execute o Script**:

```bash    
    python gerador_commit.py
```    

3. **Insira Sua Entrada**:
    
    - Quando solicitado, forneça uma descrição breve das suas alterações ou cole um trecho de código.
        
    - O script gerará uma mensagem de commit e a copiará para a área de transferência.
        
4. **Exemplo**:

```bash
    Enter the text you want to send to the Gemini API: Fixed a bug where the API returns null for invalid requests.
    Gemini API Response:
    fix(api): handle null response for invalid requests
    Response copied to clipboard.
    Application terminated.
``` 

---

## Atalhos de Teclado (Início Rápido)

### No Windows

1. **Crie um Atalho**:
    
    - Clique com o botão direito na área de trabalho ou em uma pasta e selecione **Novo > Atalho**.
        
    - No campo de localização, insira:
        
```
        pythonw.exe "C:\caminho\para\gerador_commit.py"
```     
- Substitua `C:\caminho\para\gerador_commit.py` pelo caminho real do script.
- Clique em **Avançar**, nomeie o atalho (por exemplo, `Gerador de Commit`) e clique em **Concluir**.
        
2. **Atribua um Atalho de Teclado**:
    
- Clique com o botão direito no atalho e selecione **Propriedades**.
    
- Na aba **Atalho**, clique no campo **Tecla de Atalho** e pressione a combinação de teclas desejada (por exemplo, `Ctrl + Alt + C`).
    
- Clique em **OK**.
        

Agora, você pode executar o script pressionando a combinação de teclas atribuída.

---

### No Linux

1. **Crie uma Entrada na Área de Trabalho**:
    
- Crie um arquivo `.desktop` em `~/.local/share/applications/`:
        
```bash
    nano ~/.local/share/applications/gerador_commit.desktop
```

- Adicione o seguinte conteúdo:
        
```bash
        
        [Desktop Entry]
        Name=Gerador de Commit
        Exec=python3 /caminho/para/gerador_commit.py
        Type=Application
        Terminal=true
        Icon=/caminho/para/um/icone.png
``` 
- Substitua `/caminho/para/gerador_commit.py` pelo caminho real do script e `/caminho/para/um/icone.png` por um ícone opcional.
        
2. **Atribua um Atalho de Teclado**:
    
    - Abra as configurações do sistema e navegue até **Atalhos de Teclado**.
        
    - Adicione um novo atalho personalizado:
        
        - **Nome**: `Gerador de Commit`
            
        - **Comando**: `python3 /caminho/para/gerador_commit.py`
            
        - Atribua uma combinação de teclas (por exemplo, `Ctrl + Alt + C`).
            

Agora, você pode executar o script usando a combinação de teclas atribuída.

---

## Exemplos de Mensagens de Commit

Aqui estão alguns exemplos de entradas e suas respectivas mensagens de commit:

|Entrada|Mensagem de Commit|
|---|---|
|`Adicionei uma nova funcionalidade de login`|`feat(auth): adicionar funcionalidade de login`|
|`Corrigi um bug no manipulador de respostas da API`|`fix(api): corrigir bug no manipulador de respostas`|
|`Atualizei o arquivo README`|`docs(readme): atualizar documentação`|
|`Refatorei a lógica de autenticação do usuário`|`refactor(auth): melhorar lógica de autenticação`|
|`Adicionei testes unitários para o módulo de pagamento`|`test(pagamento): adicionar testes unitários`|

---

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões, relatórios de bugs ou solicitações de funcionalidades, abra uma issue ou envie um pull request.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://LICENSE) para mais detalhes.