```mermaid
 classDiagram
      UserInterface "*" --> LoginUI
      UserInterface "*" --> LevelsUI
      Gameplay "*" --> UserInterface
      class UserInterface
      class LoginUI
      class LevelsUI
      class Gameplay
```
