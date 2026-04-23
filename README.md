# 📐 Problema do Triângulo (Triangle Problem)

Repositório contendo a implementação e a suíte de testes automatizados em Python para o clássico **Problema do Triângulo**. 

Projeto desenvolvido como requisito prático para a disciplina de **Engenharia de Software 2**.

---

## 🎓 Equipe Desenvolvedora

* **Rafaela Silva Ruis**
* **Rafael Yugo Hashimoto**
* **Ryan Augusto Ribeiro**

---

## 📝 Descrição do Problema

Dado um conjunto de três números inteiros que representam os comprimentos dos lados de um triângulo, o programa tem o objetivo de validar as regras matemáticas de existência e classificá-lo corretamente.

As saídas esperadas do programa são:

| Retorno | Regra de Negócio |
| :--- | :--- |
| **EQUILATERAL** | Todos os três lados possuem o mesmo tamanho. |
| **ISOSCELES** | Exatamente dois lados possuem o mesmo tamanho. |
| **SCALENE** | Todos os três lados possuem tamanhos diferentes. |
| **INVALID** | Os valores não formam um triângulo (ex: valores negativos, zeros, ou desrespeito à desigualdade triangular). |

---

## 🚀 Como Executar (Setup)

Siga os passos abaixo para preparar o ambiente local e rodar a bateria de testes.

**1. Crie o ambiente virtual:**
```bash
python -m venv venv
