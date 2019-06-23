def print_models(unprinted_designs,complete_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    :param unprinted_designs:
    :param complete_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model :" + current_design)
        complete_models.append(current_design)
def show_complete_models(complete_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for complete_model in complete_models:
        print(complete_model)