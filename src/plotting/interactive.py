import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_earth(radius=6371, center=(0, 0, 0), transparency=0.5):
    """
    Create a 3D graph with a perfect sphere representing the Earth at its center.

    Parameters:
    - radius (float): Radius of the Earth in kilometers (default: 6371).
    - center (tuple): Center coordinates of the Earth in 3D space (default: (0, 0, 0)).
    - transparency (float): Transparency level of the Earth (0-1), where 0 is fully transparent and 1 is opaque (default: 0.5).

    Returns:
    - fig (matplotlib.figure.Figure): The Matplotlib figure containing the 3D graph with the Earth.
    - ax (mpl_toolkits.mplot3d.Axes3D): The Axes3D object representing the 3D plot.
    """

    # Create figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Generate evenly spaced latitude and longitude points
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    u, v = np.meshgrid(u, v)

    # Convert spherical coordinates to Cartesian coordinates
    x = center[0] + radius * np.sin(v) * np.cos(u)
    y = center[1] + radius * np.sin(v) * np.sin(u)
    z = center[2] + radius * np.cos(v)

    # Plot Earth as a perfect sphere
    ax.plot_surface(x, y, z, color='b', alpha=transparency)

    # Set axis labels
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')

    ax.autoscale(enable=True, axis='both', tight=None)

    return fig, ax


def plot_orbit_ellipse(ax, inclination, raan, arg_perigee, semi_major_axis, eccentricity, center=(0, 0, 0)):
    """
    Plot an ellipse representing an orbit around the Earth on the provided Axes3D object.

    Parameters:
    - ax (mpl_toolkits.mplot3d.Axes3D): The Axes3D object representing the 3D plot.
    - inclination (float): Inclination of the orbit in degrees.
    - raan (float): Right Ascension of the Ascending Node (RAAN) in degrees.
    - arg_perigee (float): Argument of Perigee in degrees.
    - semi_major_axis (float): Semi-major axis of the orbit in kilometers.
    - eccentricity (float): Eccentricity of the orbit.
    - center (tuple): Center coordinates of the orbit in 3D space (default: (0, 0, 0)).

    Returns:
    None
    """

    # Convert angles to radians
    inclination_rad = np.radians(inclination)
    raan_rad = np.radians(raan)
    arg_perigee_rad = np.radians(arg_perigee)

    # Generate ellipse coordinates
    u = np.linspace(0, 2 * np.pi, 100)
    x = center[0] + semi_major_axis * (np.cos(u + arg_perigee_rad) * np.cos(raan_rad) - np.sin(u + arg_perigee_rad) * np.sin(raan_rad) * np.cos(inclination_rad))
    y = center[1] + semi_major_axis * (np.cos(u + arg_perigee_rad) * np.sin(raan_rad) + np.sin(u + arg_perigee_rad) * np.cos(raan_rad) * np.cos(inclination_rad))
    z = center[2] + semi_major_axis * (np.sin(u + arg_perigee_rad) * np.sin(inclination_rad))

    # Plot ellipse on the provided Axes3D object
    ax.plot(x, y, z, color='r', zorder=1)

if __name__ == "__main__":
    # Create Earth and get the Axes3D object
    earth_fig, earth_ax = create_earth(radius=6371, center=(0, 0, 0), transparency=1)

    # Plot orbit ellipse on the same Axes3D object as Earth
    #plot_orbit_ellipse(earth_ax, inclination=0, raan=45, arg_perigee=80, semi_major_axis=10000, eccentricity=0.99)

    # Display Earth and orbit ellipse
    plt.show()
