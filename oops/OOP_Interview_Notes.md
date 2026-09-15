# Python OOP — Quick Interview Revision Notes

## 1. Basics

- **OOP**: represents real-world entities as classes & objects.
- **Why OOP**: organized data storage, easy access, code reusability, easy maintenance.
- **Class**: blueprint/design used to create objects.
- **Object**: real-world entity created from a class; has attributes (data) + methods (behavior).
- **Reference variable**: a variable that refers to an object.
- **Naming rule**: Class names use PascalCase (first letter of each word capital).

```python
class ClassName:
    # variables (attributes)
    # constructor (__init__)
    # methods
```

- Create object: `obj = ClassName()`
- **Without brackets** (`e = Employee`) → `e` points to the **class** itself.
- **With brackets** (`e = Employee()`) → `e` points to an **object** (memory address).

### Accessing class variables
1. By class name: `ClassName.var`
2. By object: `obj.var`

---

## 2. Namespace / `__dict__`

- Class members are stored in a dict-like structure called **namespace** (`__dict__`).
- Each object gets **separate memory** for its own instance variables.
- Objects share class-level (common) data via the class.

---

## 3. Docstrings

- Optional description of a class, written as `"""..."""` right after `class`.
- Access via:
  - `ClassName.__doc__`
  - `help(ClassName)`

---

## 4. Class Variable Modification — IMPORTANT (common interview trap)

| Who modifies | Effect |
|---|---|
| Modify via **class name** | Affects class AND all objects (since they haven't overridden it) |
| Modify via **object** | Creates a new instance-level copy; only affects that object; breaks the link to class for that variable |
| Object modifies first, then class modifies | Object's value stays same (unaffected by later class change) — link is broken |
| Class modifies first, then object modifies | Class change reflects in all objects; then object's own change only affects itself |

**Key rule:** Once an object modifies a variable, that variable becomes independent (instance-level) and no longer follows class-level changes.

---

## 5. Types of Methods

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First argument | `self` (object) | `cls` (class) | none required |
| Accesses | Instance + class variables | Class variables only | Nothing automatically (independent) |
| Typical use | Work with object data | Alternate constructors, modify class data | Utility/helper functions |
| Call by | Object (preferred); via class needs explicit object passed | Class or Object | Class or Object |

### Instance Method
- 1st parameter always refers to the object (conventionally `self`).
- Called via object → object passed implicitly.
- Called via class name → object must be passed explicitly: `ClassName.method(obj)`.
- Passing object explicitly when calling via object itself → **error**.
- **Best practice**: inside instance methods, access class variables using `self.var` (not `ClassName.var`), so it correctly reflects any object-level overrides.

### Class Method
- Defined with `@classmethod`; first param = `cls` (the class object, not a string).
- Called via class name (preferred) or object — `cls` is passed automatically either way.
- Used for: alternative constructors, operating on/modifying class-level data.
- Cannot directly access instance attributes.
- Don't manually pass `cls`.

### Static Method
- Defined with `@staticmethod`; **no** `self` or `cls`.
- Behaves like a normal function placed inside a class (utility/helper).
- Independent of class/object — modifying class or object attributes does NOT affect its behavior/output.
- All arguments must be passed explicitly by caller.
- Can be called via class name or object.

---

## 6. Constructor (`__init__`)

- Special method, auto-executed when an object is created.
- Used to initialize instance variables.
- Two ways to invoke:
  1. Automatically: `obj = ClassName()`
  2. Manually: `ClassName.__init__(obj)`

### Types
- **Default constructor**: only `self`, no other params.
- **Parameterized constructor**: takes additional params to initialize instance variables.

### Notes
- Constructor can perform calculations, conditional logic, or even call other methods during initialization.
- Class variables declared outside `__init__` are shared; instance variables (via `self.x = x`) are per-object.

---

## 7. Method / Constructor Overloading

- **Python does NOT support true method overloading** (dynamic language — last-defined method with same name overrides earlier ones).
- If multiple methods have the same name, **only the last definition is used** — calling with fewer args than the last definition throws `TypeError`.
- **Partial workaround**: use **default arguments** (e.g., `def add(self, a=0, b=0, c=0):`) to simulate variable-argument behavior.
- **Constructor overloading**: same concept — only the last `__init__` defined is effective; use default args to simulate overloading.
- For unknown/variable number of extra arguments → use `*args`.

```python
def __init__(self, brand, model, price, *args):
    ...
```

---

## 8. Inheritance (IS-A relationship)

Definition: child class acquires properties/methods of a parent class.

### 5 Types
1. **Single level** – one child ← one parent.
2. **Multi-level** – chain: Grandparent → Parent → Child.
3. **Multiple** – one child ← multiple parents.
4. **Hierarchical** – multiple children ← one parent.
5. **Hybrid** – combination of above types.

### `super()`
- Used to call the parent class's constructor/method from the child class.
- Common pattern:
```python
class Child(Parent):
    def __init__(self, ...):
        super().__init__(...)   # calls parent constructor
        # child-specific init
```
- Also used for **method overriding** — child redefines a parent method but can still call the parent's version via `super().method_name()`.

### Method Overriding
- Child class defines a method with the **same name** as one in the parent → child's version takes priority when called on child object.
- `super().method()` inside child's override lets you still invoke the parent's version (for extending, not replacing, behavior).

---

## 9. Quick Gotchas Often Asked in Interviews

- `Employee` vs `Employee()`: class reference vs object reference.
- Why does modifying a class variable via **object** not affect other objects? → because it creates a new instance attribute shadowing the class attribute.
- Why can't you do true method overloading in Python? → it's dynamically typed; last definition wins.
- Static method ignores changes to class/instance attributes because it has no `self`/`cls` binding.
- `cls` in classmethod refers to the **class object**, not just its name as a string.
- Constructor executes automatically on object creation — no need to call it explicitly (though you technically can).
- In multi-level/multiple inheritance, `super()` follows the MRO (Method Resolution Order).
