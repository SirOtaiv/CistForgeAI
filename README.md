# 🏛️ CistForgeAI

Projeto completo para geração e reconhecimento de números cistercienses utilizando Python (OpenCV + IA) e um frontend moderno em React/NextJS.

---

## 📁 Estrutura do Projeto

```
project-root/
├── Backend/                # FastAPI - API central de orquestração
│   ├── modules/            # Pasta com os módulos relacionados aos números cistercienses
│       ├── CistForge/      # Geração de imagens a partir de números arábicos
│       └── CistMind/       # Reconhecimento de números a partir de imagem (IA)
├── Frontend/               # React/NextJS - Interface do usuário
├── Docs/                   # Documentação e anotações do projeto
```

---

## ⚙️ Tecnologias Utilizadas

- **Backend:** FastAPI
- **Frontend:** React com NextJS
- **Geração de Imagens:** OpenCV (Python)
- **Reconhecimento (IA):** KNN ou outro modelo leve com extração de features (Hu Moments, Contornos, etc)
- **Comunicação:** REST API

---

## 🎯 Objetivo

Oferecer uma aplicação que permita:

1. Converter números arábicos (inteiros) para sua forma **cisterciense**, gerando uma imagem correspondente.
2. Interpretar imagens com números cistercienses e convertê-los de volta para arábicos usando IA.
3. Exibir os resultados de forma clara no frontend, incluindo a **localização dos dígitos por quadrante**.

---

## 🚀 Como Rodar Localmente

### 1. Clonar o projeto

```bash
git clone https://github.com/SirOtaiv/CistForgeAI.git
cd CistForgeAI
```

### 2. Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
fastapi dev main.py
```

### 3. Frontend (React/Next.js)

```bash
cd frontend
npm install
npm run dev
```

### 4. Serviços

Os serviços `CistForge` e `CistMind` são usados como bibliotecas internas no backend. Rodam automaticamente junto com o FastAPI.

---

## 🔍 Funcionalidades Planejadas

- [x] Gerar imagem cisterciense a partir de número
- [x] Dividir imagem em quadrantes e identificar dígitos
- [ ] Interface para seleção de imagem e conversão para arábico
- [ ] Treinamento e uso de modelo KNN para reconhecimento
- [ ] Exibir localização dos dígitos reconhecidos

---

## 🧠 Sobre os Números Cistercienses

Sistema numérico medieval, utilizado por monges cistercienses, que representa até **9999** em uma única figura, dividida em **quatro quadrantes**:

- Superior Esquerdo: Milhares
- Inferior Esquerdo: Centenas
- Superior Direito: Dezenas
- Inferior Direito: Unidades

---

## 📜 Licença

MIT License © Otavio Murilo Rau