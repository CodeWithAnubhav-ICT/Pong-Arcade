# 🏓 Pong Arcade (High-Fidelity Physics)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Game Engine](https://img.shields.io/badge/Game_Engine-Turtle_Graphics-green?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-OOP_&_Refactoring-orange?style=for-the-badge)

> **A reconstruction of the classic Arcade Physics Engine using Python, focusing on modular class architecture and dynamic speed scaling.**

---

## 🔄 The Logic Story (Day 22)
While procedural Pong is common, **Day 22** was about building a robust system that handles high-speed collisions without visual flicker. The architecture was designed to transition from a simple game to a precise coordinate-based simulation.

* **The Collision Geometry Problem:** Unlike Snake, Pong requires detecting intersections between a moving point (Ball) and a moving segment (Paddle).
* **Stability Logic:** I implemented logic that checks for a proximity "collision zone" rather than exact pixel matching to ensure stability at high speeds.
* **Dynamic Difficulty Scaling:** To prevent a stagnant game state, I integrated a compound scaling factor where every paddle hit triggers a **10% reduction** in the screen refresh delay, effectively increasing the ball's velocity.
* **Manual Rendering:** I bypassed the default `turtle` animation cycle using `screen.tracer(0)`. This allows the "Architect" to control exactly when the frame updates, eliminating flickering and ensuring "pin-point perfect" movement.

---

## 🏗️ System Architecture
The codebase is decoupled into four primary modules to ensure high maintainability:

| Class | Type | Responsibility |
| :--- | :--- | :--- |
| **`Paddle`** | `Object Controller` | Encapsulates positional state and boundary constraints for dual-axis movement. |
| **`Ball`** | `Physics Engine` | Manages velocity vectors, wall-bounce logic, and difficulty scaling math. |
| **`Scoreboard`** | `State Manager` | Tracks the live game state and renders the UI in real-time. |
| **`main`** | `Orchestrator` | Manages the high-frequency game loop and cross-class communication. |

---

## 🛠️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/CodeWithAnubhav-ICT/Pong-Arcade.git](https://github.com/CodeWithAnubhav-ICT/Pong-Arcade.git)
    ```
2.  **Run the application:**
    ```bash
    python main.py
    ```

## 🎮 Controls
* **Right Player**: ⬆️/⬇️ Arrow Keys
* **Left Player**: **'W'** / **'S'** Keys

---
*Part of my [100 Days of Code Journey](https://github.com/CodeWithAnubhav-ICT/100_Days_Of_Python_Bootcamp).*
