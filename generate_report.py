
import hclw_data_sifter
import naver_hclw_data_sifter
from PIL import Image
def generate_image():
    data = hclw_data_sifter.get_data()
    arcs_data = hclw_data_sifter.get_arcs_data(data)
    hclw_data_sifter.get_stats(data)
    image = hclw_data_sifter.generate_report_image(arcs_data)
    naver_data = naver_hclw_data_sifter.get_data()
    naver_arcs_data = naver_hclw_data_sifter.get_arcs_data(naver_data)
    naver_hclw_data_sifter.get_stats(naver_data)
    naver_image = naver_hclw_data_sifter.generate_report_image(naver_arcs_data)
    report_image = Image.new(mode = "RGB", size = naver_image.size, color="WHITE")
    report_image.paste(naver_image, (0, 0))
    report_image.paste(image, (0,0))
    report_image.save("./images/hclw_data.png")

if __name__ == "__main__":
    generate_image()