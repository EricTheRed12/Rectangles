## Requirements:
Python >= 3.9 

## To run:
python3 main.py

### Rectangle Class
| Arguments | Type | Description |
| :--- | :--- | :--- |
| `width` | `Int/Float` | width of the rectangle. |
| `height` | `Int/Float` | height of the rectangle. |
| `center` | `List of Int/Float` | list of length 2 representing the center of the rectangle. |

| Variables | Type | Description |
| :--- | :--- | :--- |
| `center` | `List of Int/Float` | list of length 2 representing the center of the rectangle. |
| `center` | `List of Int/Float` | list of length 2 representing the center of the rectangle. |
| `left` | `Int/Float` | value representing left side of rectangle |
| `right` | `Int/Float` | value representing right side of rectangle |
| `top` | `Int/Float` | value representing top side of rectangle |
| `bottom` | `Int/Float` | value representing bottom side of rectangle |

#### Throws
- **`RectangleError`**: If invalid center type or length
- **`RectangleError`**: If center values are the incorrect type
- **`RectangleError`**: If the width is invalid
- **`RectangleError`**: If the height is invalid 

#### Example

    rect1 = Rectangle(5, 10, (10, 10))


### Intersection
| Arguments | Type | Description |
| :--- | :--- | :--- |
| `rectangle` | `Rectangle` | Rectangle object to check if the current rectangle intersects. |

| Returns | Type | Description |
| :--- | :--- | :--- |
| `intersection` | `Boolean` | boolean representing the intersection status. |
| `points` | `List of ints/floats` | List of points representing the intersection rectangle. |
#### Throws
- **`RectangleError`**: If second rectangle is not a valid `Rectangle`.

#### Example

    intersected, points = rect1.intersection(rect2)

### Containment
| Arguments | Type | Description |
| :--- | :--- | :--- |
| `rectangle` | `Rectangle` | Rectangle object to check if the current rectangle is contained within. |

| Returns | Type | Description |
| :--- | :--- | :--- |
| `contained` | `Boolean` | boolean representing the containment status. |
#### Throws
- **`RectangleError`**: If second rectangle is not a valid `Rectangle`.

#### Example

    contained = rect1.containment(rect2)

### Adjacent
| Arguments | Type | Description |
| :--- | :--- | :--- |
| `rectangle` | `Rectangle` | Rectangle object to check if the current rectangle is adjacent. |

| Returns | Type | Description |
| :--- | :--- | :--- |
| `adjacent` | `Boolean` | boolean representing the adjacent status. |
the intersection rectangle. |
#### Throws
- **`RectangleError`**: If second rectangle is not a valid `Rectangle`.

#### Example

    adjacent = rect1.adjacent(rect2)