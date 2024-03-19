
##################################################################################
##################" have_a_plot hand Version (HP) is a for Tello #################
##################             working librairy                  #################
##################  that plot in real time the drone position on #################
##################              a virtual space                  #################
##################            based on the inputs                #################
##################################################################################




from djitellopy import Tello
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
import json




def init():
    global x_list, y_list, z_list
    x_list = []
    y_list = []
    z_list = []

    global x_velo, y_velo, z_velo
    x_velo = 0.0
    y_velo = 0.0
    z_velo = 0.0


def plot_the_3D():
    fig = plt.figure()
    global axex3D
    axex3D = fig.add_subplot(111, projection='3d')
    plt.ion()  # Turn on interactive mode for real-time plotting
    plt.show()


def refresh_coo(x_velo, y_velo, z_velo):
    global x_list, y_list, z_list


    x_list.append(x_velo)
    y_list.append(y_velo)
    z_list.append(z_velo)
    axex3D.clear()
    axex3D.plot3D(x_list, y_list, z_list, 'blue')
    plt.draw()
    plt.pause(0.01)  # Pause to allow the plot to update

    # Save coordinates to a JSON file
    #save_coordinates_to_json()


def save_coordinates_to_json():
    global x_list, y_list, z_list

    coordinates = {"x": x_list, "y": y_list, "z": z_list, "heure" : str(datetime.now())}

    with open("data\coordinates.json", "w") as json_file:
        json.dump(coordinates, json_file)


def end():
    plt.ioff()
    plt.show()


