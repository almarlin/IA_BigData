from empresa import Empresa

def main():
    # Crear una empresa
    empresa = Empresa("MiEmpresa",0)

    # 1. Cargar cinco empleados iniciales si no existen
    if not empresa.empleados:
        print("Cargando empleados iniciales...")
        for i in range(1, 6):
            empresa.nuevo_empleado(f"Empleado{i}", 3000 + i * 500)

    # Mostrar empleados actuales
    print("\nEmpleados iniciales:")
    empresa.mostrar_empleados()

    # 2. Dar de alta a dos empleados adicionales
    print("\nAgregando dos nuevos empleados...")
    empresa.nuevo_empleado("Carlos", 4500)
    empresa.nuevo_empleado("Laura", 5000)

    # Mostrar empleados después de alta
    print("\nEmpleados después de agregar:")
    empresa.mostrar_empleados()

    # 3. Dar de baja a un empleado
    print("\nDespidiendo a un empleado...")
    empleado_a_despedir = empresa.empleados[0]
    empresa.despedir_empleado(empleado_a_despedir)

    # Mostrar empleados después de baja
    print("\nEmpleados después de despido:")
    empresa.mostrar_empleados()

main()
