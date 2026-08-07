 path = Path('')
    items  = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")