# 
# * ---------------------- *
#     INSTALACIÓN DE ROS
# * ---------------------- *
# 
# Para instalar ROS es necesario tener Ubuntu 20.04 LTS en wsl. Se puede encontrar fácilmente en la Microsoft Store
# Posteriormente e la instalación, ejecutar los siguientes comandos:
# ```
# sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
# sudo apt update
# sudo apt install -y ros-noetic-desktop python3-rosdep
# sudo rosdep init
# rosdep update 
# ```
# Una vez actualizado ROS ejecutar estos comandos para añadirlo al path de Ubuntu y añadir una herramienta para instalar dependencias 
# ```
# echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
# source ~/.bashrc
# sudo apt install python3-rosdep
# ```
# Para iniciar rosdep ejecutar:
# ```
# sudo rosdep init
# rosdep update
# ```
# 
# * ---------------------------- *
#     INSTALACIÓN DE TurtleBot
# * ---------------------------- *
# 
# Instalar los paquetes necesarios para turtlebot:
# ```
# sudo apt install ros-noetic-turtlebot3 ros-noetic-turtlebot3-bringup
# ```
# 
# Configurar y elegir el modelo de TurtleBot:
# ```
# echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
# source ~/.bashrc
# ```
# 
# Los modelos disponibles son burguer/waffle/waffle_pi
# 
# * ------------------------ *
#     INSTALACIÓN DE Gazebo
# * -------------------------*
# Para la simulacion del robot es necesario Gazebo
# ```
# sudo apt install ros-noetic-turtlebot3-gazebo
# ```
# Se puede poner en marcha la simulacion con 
# ```
# roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
# ```
# 
# * ----------------------- * 
#     ESPACIO DE TRABAJO
# * ----------------------- *
# 
# Para poder ejecutar el fichero python debemos crear un espacio de trabajo y añadirlo a ROS
# Antes de eso debemos instalar un compilador de C++ pues la mayoria de paquetes ROS estan en ese lenguaje y algunas dependencias adicionales
# ```
# sudo apt install build-essential
# sudo apt install ros-noetic-desktop-full
# ```
# Creamos la carpeta
# ```
# mkdir -p ~/catkin_ws/src
# cd ~/catkin_ws/
# catkin_make
# ```
# Agregar la carpeta al bashrc en otra terminal
# ```
# echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
# source ~/.bashrc
# ```
# Creamos el paquete Turtlebot_control con las dependencias rospy y geometry_msgs
# ```
# catkin_create_pkg turtlebot_control rospy std_msgs geometry_msgs
# ```
# Crear carpeta scripts en src y añadir el codigo python
# ```
# mkdir /src/scripts
# nano ros_MartinezLineros_Alvaro.py
# ```
# Ahora para poder ejecutarlo tenemos que darle permisos
# ```
# chmod +x ros_MartinezLineros_Alvaro.py
# ```
# Finalmente ejecutamos el fichero python con
# ```
# rosrun turtlebot_control ros_NombreAlumno.py
# ```


# ---- CODIGO TURTLEBOT ------------------------

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_in_line():
    # Iniciar el nodo de ROS
    rospy.init_node('move_robot', anonymous=True)

    # Publicador de comandos al robot
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Esperar un poco para asegurar que el publicador esté listo
    rospy.sleep(1)

    # Crear mensaje Twist para controlar el movimiento
    move_cmd = Twist()

    # Mover en línea recta
    rospy.loginfo("Moviendo en línea recta")
    move_cmd.linear.x = 0.2  # Velocidad en m/s hacia adelante
    move_cmd.angular.z = 0.0  # Sin rotación

    # Publicar el mensaje para mover el robot
    pub.publish(move_cmd)
    rospy.sleep(2)  # Mover por 2 segundos

    # Detener el robot
    move_cmd.linear.x = 0.0
    pub.publish(move_cmd)
    rospy.sleep(1)

    # Girar 90 grados
    rospy.loginfo("Girando 90 grados")
    move_cmd.angular.z = 0.5  # Velocidad angular para girar en radianes/s
    pub.publish(move_cmd)
    rospy.sleep(2)  # Girar durante 2 segundos

    rospy.loginfo("Moviendo en línea recta")
    move_cmd.linear.x = 0.2  # Velocidad en m/s hacia adelante
    move_cmd.angular.z = 0.0  # Sin rotación
    
    # Detener el robot
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)
    rospy.sleep(1)

    rospy.loginfo("Movimiento y giro completados")

if __name__ == '__main__':
    try:
        move_in_line()
    except rospy.ROSInterruptException:
        pass

