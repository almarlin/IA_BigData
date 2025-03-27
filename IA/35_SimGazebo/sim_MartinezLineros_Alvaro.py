#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def move_to_goal(x, y, z=0.0, frame_id='map'):
    """
    Mueve el robot a una posición objetivo dada en el marco de referencia del mapa.
    :param x: Coordenada X del objetivo.
    :param y: Coordenada Y del objetivo.
    :param z: Coordenada Z (default a 0.0 para el plano 2D).
    :param frame_id: El marco de referencia (por defecto 'map').
    """
    rospy.init_node('move_to_goal_node', anonymous=True)
    
    # Publicador del objetivo
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
    # Espera a que se establezca la conexión con el tópico
    rospy.sleep(1)
    
    # Crear el mensaje PoseStamped
    goal = PoseStamped()
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = frame_id

    # Establecer la posición objetivo
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = z
    
    # Establecer la orientación (no tiene importancia en un plano 2D)
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0

    # Publicar el objetivo
    rospy.loginfo("Enviando objetivo a (%f, %f)", x, y)
    pub.publish(goal)

if __name__ == '__main__':
    try:
        # Llama a la función con la posición objetivo deseada (ej. x=1.0, y=2.0)
        move_to_goal(1.0, 2.0)
        rospy.spin()  # Mantiene el nodo funcionando mientras el robot se mueve
    except rospy.ROSInterruptException:
        pass
