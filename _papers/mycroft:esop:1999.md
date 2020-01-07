@InProceedings{10.1007/3-540-49099-X_14,
author="Mycroft, Alan",
editor="Swierstra, S. Doaitse",
title="Type-Based Decompilation (or Program Reconstruction via Type Reconstruction)",
booktitle="Programming Languages and Systems",
year="1999",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="208--223",
abstract="We describe a system which decompiles (reverse engineers) C programs from target machine code by type-inference techniques. This extends recent trends in the converse process of compiling high-level languages whereby type information is preserved during compilation. The algorithms remain independent of the particular architecture by virtue of treating target instructions as register-transfer specifications. Target code expressed in such RTL form is then transformed into SSA form (undoing register colouring etc.); this then generates a set of type constraints. Iteration and recursion over data-structures causes synthesis of appropriate recursive C structs; this is triggered by and resolves occurs-check constraint violation. Other constraint violations are resolved by C's casts and unions. In the limit we use heuristics to select between equally suitable C code --- a good GUI would clearly facilitate its professional use.",
isbn="978-3-540-49099-9"
}

