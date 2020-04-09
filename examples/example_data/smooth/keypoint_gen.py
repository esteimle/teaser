import open3d as o3d
import numpy as np

if __name__ == "__main__":
	print("Opening PLY file")
	pcd = o3d.io.read_point_cloud("cloud_bin_0.ply")
	xyz_load = np.asarray(pcd.points)
	print(xyz_load.size)
	print(pcd)
	print("opened file")

	number_of_points = xyz_load.size / 3

	traindata_path = 'test_keypoints.txt'
	with open(traindata_path, "w") as f:
		for i in range(1000):
			index = np.random.randint(0, number_of_points)
			f.writelines(str(index))
			f.writelines('\n')
