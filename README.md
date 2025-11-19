# Lab Overview

This lab focuses on transforming a procedural-style drawing program into a clean and modular Object-Oriented Programming (OOP) in Python to generate
polygon-based artwork using the `turtle` graphics module. The program shows the effect of
randomized properties such as color, size, orientation, and position.

## Project Structure

### polygon_art

- `README.md`: This readme file  
- `oop_version.py`: The main polygon art generator program.
- `procedural.py`: The procedural version of the program.
- `art`: This folder contains the example of the art in each choice.

## Design Overview

### Polygon Class

Located in `oop_version.py`, the `Polygon` class represents a geometric polygon.

**Attributes**
- `num_sides` (int): Number of sides of the polygon  
- `num_inside` (int): How many polygons to draw inside  
- `size` (int): Randomized polygon side length  
- `orientation` (int): Random rotation angle  
- `location` (list[int, int]): Random initial coordinate  
- `color` (tuple): Random RGB color  
- `border_size` (int): Random border thickness  

**Methods**
- `get_new_color(self)`: Generate and return a random RGB color  
- `draw_polygon(self)`: Draw a single polygon using turtle  
- `draw(self)`: Draw the original polygon and, if specified, additional nested polygons

### Program Flow

The main program prompts the user to choose an art mode (1–9). Each mode creates
different polygon patterns:

- Mode 1: Only triangles  
- Mode 2: Only squares  
- Mode 3: Only pentagons  
- Mode 4: Random 3–5 sided polygons  
- Mode 5–8: Same as above but with nested polygons  
- Mode 9: Random polygons with random nested behavior  

## Running the Code

To run the polygon art generator, execute:

```bash
python oop_version.py
