  ```mermaid
  classDiagram
  %% https://wecanpanic.hatenablog.com/entry/2022/06/19/%E3%82%82%E3%81%86%E4%BF%BA%E3%81%8CMermaid%E3%81%AE%E3%83%81%E3%83%BC%E3%83%88%E3%82%B7%E3%83%BC%E3%83%88%E3%82%92%E4%BD%9C%E3%82%8B%EF%BC%88%E3%82%AF%E3%83%A9%E3%82%B9%E5%9B%B3%EF%BC%89
  
  %% Original typeの宣言
  class Id { -int value }
  class Name { -string value }
  class Age { -int value }

  %% Enum型の宣言
  class UserType {
    Employee
    Customer
    Administrator
  }
  <<enumeration>> UserType
  %% <<>> の中は何を書いても通る

  %% クラス
  %% クラス内の変数等の書き方は自由（id: Id 等もOK）
  class User {
    +Id id
    +Name name
    +Age age
    -UserType type
    +regist()
    +greeting()
  }
  <<interface>> User

  class EmployeeUser {
    +Id id
    +Name name
    +Age age
    +regist()
    +greeting()
  }

  %% 関係性
  User <|-- EmployeeUser: extends
  User o-- Id
  User o-- Name
  User o-- Age
  User o-- UserType
  ```
