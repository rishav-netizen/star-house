<p align="center">
  <picture>
    <source srcset="assets/house_logo.svg" type="image/svg+xml">
    <img src="assets/house_logo.png" width="90" alt="ASCII House Logo" />
  </picture>
</p>

<h1 align="center">Procedural ASCII House Generator</h1>

<p align="center">
  <em>A modular, dynamically scaled ASCII architecture generator implemented in pure C.</em>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-C99-00599C?logo=c&logoColor=white" alt="Language" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Course-Semester%201%20C%20Programming-orange" alt="Course" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Assignment-ASCII%20Architecture-brightgreen" alt="Assignment" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey" alt="Platform" /></a>
</p>

> Give it a height ($n \ge 6$) and watch it procedurally engineer pitched roofs, symmetrical dual windows, structural walls, a centered doorway, and a sturdy foundation.

---

## 📸 Visual Showcase

Here is an architectural render generated with **Size 6**:

```text
          *                     
         * *         
       * * * *       
     * * * * * *     
   * * * * * * * *   
 * * * * * * * * * * 
 *                 *
 *                 *
 *   ***     ***   *
 *   ***     ***   *
 *                 *
 *                 *
 *      *****      *
 *      *   *      *
 *      *   *      *
 *      *   *      *
 * * * * * * * * * *
```

And scaled up with **Size 8**:

```text
              *                             
             * *             
           * * * *           
         * * * * * *         
       * * * * * * * *       
     * * * * * * * * * *     
   * * * * * * * * * * * *   
 * * * * * * * * * * * * * * 
 *                         *
 *                         *
 *    ****         ****    *
 *    ****         ****    *
 *                         *
 *                         *
 *        *********        *
 *        *       *        *
 *        *       *        *
 *        *       *        *
 *        *       *        *
 * * * * * * * * * * * * * *
```

---

## ✨ Key Features

- 📐 **Dynamic Parametric Scaling**: All house proportions (roof slope, wall clearance, window spans, door clearance, and foundation width) dynamically compute from a single variable: `height`.
- 🧩 **Modular Procedural Design**: Built with clean, single-responsibility functions (`roof`, `mid`, `windows`, `doors`, `baseline`).
- ⚖️ **Parity Correction**: Custom window spacing compensation for even vs. odd dimensions ensures bilateral symmetry.
- 🛡️ **Defensive Validation**: Guards against invalid inputs by enforcing a minimum height constraint ($height \ge 6$).
- ⚡ **Zero External Dependencies**: Pure standard C (`stdio.h`, `stdlib.h`), compiling instantly on any modern C compiler.

---

## 🏗️ Architectural Component Breakdown

```
        ▲        --> Roof Peak & Symmetrical Slopes (roof)
       / \       
      /   \      
     /_____\     
     |     |     --> Upper Wall Clearance (mid)
     | [ ] |     --> Symmetrical Dual Windows (windows)
     |     |     --> Inter-story Wall Clearance (mid)
     |  _  |     --> Centered Doorway & Transom (doors)
     | | | |     
     =======     --> Ground Foundation Line (baseline)
```

### Mathematical Proportions

| Architectural Element | Function | Formulas & Dimensions |
|:---|:---|:---|
| **Pitched Roof** | `roof(int height)` | Peak apex at $2h - 2$ spaces; slopes span $h$ levels with interleaved star patterns (`star` and `star_`). |
| **Clearance Walls** | `mid(int height)` | Spans $\lfloor h / 3 \rfloor$ vertical rows. Width interior is $4h - 7$ blank spaces bounded by single star columns. |
| **Dual Windows** | `windows(int height)` | Spans $\lfloor h / 3 \rfloor$ vertical rows. Each window width is $\lfloor h / 2 \rfloor$ stars. Central deduction offset is $7$ for even $h$ and $5$ for odd $h$. |
| **Entrance Door** | `doors(int height)` | Door lintel header spans $2h - 7$ stars. Door height spans $\lfloor 3h / 5 \rfloor$ rows with a $2h - 9$ inner opening. |
| **Foundation Base** | `baseline(int height)` | Spans $2h - 2$ star-space pairs for a solid footer. |

---

## 📁 Repository Structure

```tree
star-house/
├── assets/         # Project logos and visual assets
├── house.c         # Primary interactive application (prompts user for size)
├── house_cmd.c     # CLI argument version (accepts size via argv: ./house <size>)
└── README.md       # Project documentation
```

### File Details

- **[`house.c`](house.c)**: Prompts the user via `scanf` with a validation loop (`get_positive_int()`) requiring a minimum size of 6, then renders the complete building.
- **[`house_cmd.c`](house_cmd.c)**: Command-line interface alternative that reads the height directly from `argv[1]`.

---

## 🚀 Getting Started

### Prerequisites

You only need a C compiler installed on your system:
- **macOS**: `clang` / `gcc` (included in Apple Xcode Command Line Tools)
- **Linux**: `gcc` (`sudo apt install build-essential`)
- **Windows**: `gcc` via MinGW or WSL

### Compilation & Running

#### 1. Interactive Version (`house.c`)

Compile with standard optimizations:
```bash
gcc -Wall -Wextra -O2 house.c -o house
```

Run the binary:
```bash
./house
```

**Example Run:**
```console
$ ./house
Size?(min 6): 6
```

---

#### 2. Command-Line Version (`house_cmd.c`)

> [!TIP]
> Ensure the `main` signature in `house_cmd.c` is written as `int main(int argc, char *argv[])` so command-line arguments parse cleanly with `atoi`.

Compile:
```bash
gcc -Wall -Wextra -O2 house_cmd.c -o house_cmd
```

Run with arguments:
```bash
# Valid run
./house_cmd 7

# Validation check for small sizes
./house_cmd 4
# Output: Size too less!
```

---

## 🧠 Concepts Demonstrated

- **Control Flow & Loops**: Nested loops (`for`, `while`, `do-while`) for multi-dimensional coordinate spaces.
- **Parametric Geometry**: Translation of geometric blueprints into integer arithmetic equations.
- **Function Decomposition**: Deconstruction of a complex visual output into clean, reusable modular units.
- **Input Sanitization**: Handling boundary conditions and user error constraints.

---

## 📜 License

Created as part of the Semester 1 C Programming coursework. Feel free to use, modify, and build upon this code for educational and hobby projects!
