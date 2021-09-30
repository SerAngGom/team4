# A 

curso_compañero == 1 and grado_compañero == 'videojuegos'

# B

curso_compañero != 1 and grado_compañero != 'videojuegos'
not (curso_ compañero == 1 and grado_compañero == 'videojuegos')


# C

grado_compañero == 'enfermeria' or grado_compañero == 'medicina' or grado_compañero == 'psicologia'

# D

grado_compañero != 'enfermeria' and grado_compañero != 'medicina' and grado_compañero != 'psicologia'
not (grado_compañero == 'enfermeria' or  grado_compañero == 'medicina' or grado_compañero == 'psicologia')

# E

grado_compañero == mi_grado and curso_compañero == mi_curso


# F

curso_compañero != mi_curso and grado_compañero == mi_grado
not curso_compañero == mi_curso and not grado_compañero != mi_grado

# G

curso_compañero == mi_curso and grado_compañero != mi_grado
