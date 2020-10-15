Нарушены прицнипы:
+ Single responsibility
Класс Administrator слишком много посторонних функций, которые выполняют различные задачи

+ Open-closed principle
Класс Administrator выполняет слишком много функций, которые не ясно, чем дополнить. Правильнее было бы сделать один родительский класс - а каждый из методов Administrator вводился в дочерних классах.

+ Liskov substitution principle
Класс Administrator и Student возвращают разные типы данных
