# Sistema de Cadastro de Pets 🐾

Projeto Final – Desenvolvimento Web II
**Autores:** Otávio Sousa da Silva e Guilherme Pablo de Sousa Silva

---

## 📌 Sobre o Projeto

Este projeto consiste em um sistema completo de **Cadastro de Pets**, desenvolvido utilizando **Flask**, **SQLAlchemy**, **HTML**, **CSS** e **JavaScript**.
O sistema permite realizar operações completas de **CRUD**: cadastrar, visualizar, editar e excluir pets, além de filtrar e buscar registros.

O objetivo foi integrar frontend e backend, utilizando rotas, templates, persistência de dados e uma interface responsiva.

---

## ✅ Funcionalidades Implementadas

### 🔹 CRUD Completo

* Adicionar novos pets
* Listar todos os pets cadastrados
* Editar informações de um pet
* Excluir pets do banco de dados

Todas as ações atualizam diretamente o banco usando SQLAlchemy.

### 🔹 Persistência com SQLAlchemy

* Classe `Pet` representando a tabela
* Integração com o Flask via ORM
* Banco SQLite para fácil uso e portabilidade

### 🔹 Formulários GET e POST

* Cadastro e edição através de formulários HTML
* Métodos GET/POST corretamente utilizados
* Validação básica feita com HTML e JavaScript

### 🔹 Templates com Jinja2

* Estrutura separada entre lógica (controllers) e apresentação (templates)
* Uso de `for`, `if`, blocos extendidos e variáveis

### 🔹 Estilização com CSS

* Layout responsivo com Flexbox
* Arquivo `style.css` dedicado
* Ícones e botões bem organizados

### 🔹 JavaScript Integrado

* Filtro de busca funcionando em tempo real
* Função dinâmica manipulando elementos do DOM

### 🔹 Busca e Filtragem

* Campo de busca por nome do pet
* Filtragem instantânea com JavaScript

### 🔹 Uso de Imagens

* Cada pet possui uma imagem associada
* Exibidas nos templates
* Armazenamento via pasta `/static/img`

---

## 📁 Estrutura do Projeto

```
/projeto_final
│
├── controllers/
│   └── views.py
│
├── models/
│   └── modelo.py
│
├── templates/
│   ├── index.html
│   └── editar.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       └── (imagens dos pets)
│
├── README.md
└── run.py

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **Flask**
* **SQLAlchemy**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Jinja2**
* **SQLite**
