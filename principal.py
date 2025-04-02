import Models.clase as c
import controllers.dao_controller as dao

materia = c.Materia("Calculo", "MAT101", 4)

dao = dao.MateriaDao()
dao.agregar_materia(materia)
dao.obtener_materias()