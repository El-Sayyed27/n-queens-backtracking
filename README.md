# ♛ N-Queens Backtracking Visualized

A beginner-friendly Python implementation of the classic **N-Queens problem** using **backtracking** and a **2D array representation** of the chessboard.

This project is designed to help learners understand how recursion and backtracking work step by step to generate all valid solutions.

---

## 📌 Problem Statement

Place **N queens** on an **N × N chessboard** such that:

- No two queens share the same **row**
- No two queens share the same **column**
- No two queens share the same **diagonal**

---

## 🧠 Approach

This project uses:

### 🔁 Backtracking Algorithm
- Place one queen per row
- Try all columns in that row
- If placement is safe → move to next row
- If not safe → backtrack and try another position

### 🧾 Board Representation
- `"Q"` → Queen
- `"."` → Empty cell

Example (N = 4):

- `.  Q  .  .`
- `.  .  .  Q`
- `Q  .  .  .`
- `.  .  Q  .`

  
---

## ⚙️ How It Works

1. Start from row 0
2. Try placing a queen in each column
3. Check if the position is safe
4. If safe, recursively move to the next row
5. If a solution is found, store it
6. Backtrack and explore other possibilities

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/n-queens-backtracking-visualized.git
