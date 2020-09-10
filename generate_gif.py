"""
Generate gif from images.
"""
import argparse
import os.path as path
try:
    import imageio
except ImportError:
    raise ImportError("Please install imageio by: pip3 install imageio")

parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')
parser.add_argument('-f', '--folder', default='/Users/melody/Downloads/test', type=str, metavar='PATH')
parser.add_argument('-o', '--out', default='result.gif', type=str)
parser.add_argument('-n', '--number', default=100, type=int)
parser.add_argument('--prefix', default='epoch_', type=str)
parser.add_argument('--suffix', default='.png', type=str)
parser.add_argument('--fps', default=3, type=int)

args = parser.parse_args()


def main():
    outfile_name = path.join(args.folder,args.out)
    gif_images = []
    for i in range(1, args.number+1):
        image_path = args.prefix+str(i)+args.suffix
        image_path = path.join(args.folder, image_path)
        if path.exists(image_path):
            gif_images.append(imageio.imread(image_path))
        else:
            print(f"Image {image_path} not exists. Ignored.")
    imageio.mimsave(outfile_name, gif_images, fps=args.fps)
    print("Done!")


if __name__ == '__main__':
    main()
