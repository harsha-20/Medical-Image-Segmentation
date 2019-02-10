def custom_image_generator(generator, data_x, data_y, seed, batch_size=16):


    iterator = generator.flow(data_x, data_y,
                              batch_size=batch_size,
                              seed=seed,
                              shuffle=True)

    for batch_x, batch_y in iterator:

        yield batch_x, batch_y