import numpy as np
import matplotlib.pyplot as plt

def draw_manipulator(link_lengths, joint_angles):
    # Define the base of the manipulator
    base = np.array([0, 0])

    # Compute the positions of each joint
    positions = [base]
    current_angle = 0
    current_position = base

    for i, (length, angle) in enumerate(zip(link_lengths, joint_angles)):
        current_angle += angle  # Update the angle with the joint angle
        dx = length * np.cos(current_angle)
        dy = length * np.sin(current_angle)
        next_position = current_position + np.array([dx, dy])
        positions.append(next_position)
        current_position = next_position

    # Extract x and y coordinates
    positions = np.array(positions)
    x_coords, y_coords = positions[:, 0], positions[:, 1]

    # Plot the manipulator
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, '-o', linewidth=2, markersize=8, label="Links")

    # Annotate the angles
    for i, (pos, angle) in enumerate(zip(positions[:-1], joint_angles)):
        plt.text(pos[0], pos[1], f"\u03B8{i+1}", fontsize=12, ha='right')

    # Configure plot
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    plt.title('3-Link Manipulator with Angle Conventions', fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.legend()
    plt.show()

# Define the lengths of the links and the joint angles
link_lengths = [2, 1.5, 1]  # Lengths of the manipulator links
joint_angles = [np.pi / 4, -np.pi / 6, np.pi / 3]  # Joint angles in radians

# Draw the manipulator
draw_manipulator(link_lengths, joint_angles)
