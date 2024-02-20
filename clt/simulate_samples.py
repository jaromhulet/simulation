import numpy as np
from matplotlib import pyplot as plt


def simulate_samples(num_samples,
                     distribution,
                     dist_attrs,
                     plot_title = ''):

    '''
        creates multiple sample means to show that they converge 
        into a normal distribution - this is a demonstration
        of the CLT

        inputs:
            num_samples (int)          : the number of random samples created
            distribution (func)        : the function used to randomly sample
                                         from a probability distribution
            dist_attrs (dict)          : dictionary of the needed inputs 
                                         for the distibution function
            plot_title (str, optional) : title for histogram

    '''

    sample_means = []

    for i in range(num_samples):
        temp_sample = distribution(*dist_attrs)
        temp_sample_mean = np.mean(temp_sample)
        sample_means.append(temp_sample_mean)

    plt.hist(sample_means)
    plt.title(plot_title)
    plt.show()

    print('done')

    return

# show CLT for normal distribution
simulate_samples(1000, np.random.normal, {5, 1000}, 'normal distribution')

# show CLT for uniform distribution
simulate_samples(1000, np.random.uniform, {0, 100, 1000}, 'uniform distribution')

# show CLT for exponential distribution
simulate_samples(10000, np.random.exponential, {10, 1000}, 'exponential distribution')

# show CLT for poisson distribution
simulate_samples(10000, np.random.poisson, {0.3, 1000}, 'poisson distribution')

