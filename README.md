# 📐 Problema do Triângulo (Triangle Problem)

Repositório contendo a implementação em Python e a suíte de testes automatizados (`pytest`) para o clássico **Problema do Triângulo**.

Projeto desenvolvido como requisito prático para a disciplina de **Engenharia de Software 2**.

---

## 🎓 Equipe Desenvolvedora

* Rafaela
* Rafael
* Ryan

---

## 📝 Descrição do Problema

Dado um conjunto de três números inteiros que representam os comprimentos dos lados de um triângulo, o programa valida as regras matemáticas de existência e o classifica corretamente. 

### Classificação Principal

| Retorno | Regra de Negócio |
| :--- | :--- |
| **EQUILATERAL** | Todos os três lados possuem o mesmo tamanho. |
| **ISOSCELES** | Exatamente dois lados possuem o mesmo tamanho. |
| **SCALENE** | Todos os três lados possuem tamanhos diferentes. |
| **INVALID** | Os valores não formam um triângulo (ex: valores nulos, negativos ou que violam a desigualdade triangular). |

### Verificação Adicional: Triângulo Retângulo

O sistema também conta com a propriedade `is_right`, que valida se o triângulo formado possui um ângulo reto (90 graus). A verificação é feita ordenando os lados e aplicando o **Teorema de Pitágoras** (cateto² + cateto² = hipotenusa²), onde o maior lado assumido é sempre a hipotenusa.

---

## 🚀 Como Executar (Setup e Testes)

Siga os passos abaixo para preparar o ambiente local e rodar a bateria de testes automatizados.

**1. Crie o ambiente virtual:**
```bash
python -m venv venv
```

**2. Ative o ambiente virtual:**
* **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```
* **Windows:**
  ```bash
  venv\Scripts\activate
  ```

**3. Instale as dependências:**
```bash
pip install pytest
```

**4. Execute os testes:**
Para rodar todos os testes com detalhamento no terminal, utilize:
```bash
pytest -v
```
