def convert_to_model_scale(real_size_meters, scale):
    """
    Converts a real-world measurement in meters into a model measurement in centimeters.

    Example:
    4 meters at scale 1:20 becomes 20 cm.
    """
    model_size_meters = real_size_meters / scale
    model_size_cm = model_size_meters * 100
    return model_size_cm


def main():
    print("ArchFlow Scale Converter")
    print("------------------------")

    real_size = float(input("Enter real size in meters: "))
    scale = int(input("Enter scale, for example 20 for 1:20: "))

    result = convert_to_model_scale(real_size, scale)

    print(f"{real_size} m in scale 1:{scale} = {result:.2f} cm")


if __name__ == "__main__":
    main()
