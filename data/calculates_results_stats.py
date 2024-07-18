def calculates_results_stats(results_dic):
    results_stats = dict()

    results_stats['n_images'] = len(results_dic)
    results_stats['n_dogs_img'] = 0
    results_stats['n_notdogs_img'] = 0
    results_stats['n_correct_dogs'] = 0
    results_stats['n_correct_notdogs'] = 0
    results_stats['n_correct_breed'] = 0

    for key in results_dic:
        if len(results_dic[key]) >= 4:  # Vérifie que la liste a au moins 4 éléments
            if results_dic[key][3] == 1:  # image 'is-a' dog
                results_stats['n_dogs_img'] += 1

                if results_dic[key][4] == 1:  # Correctly classified dog
                    results_stats['n_correct_dogs'] += 1

                if results_dic[key][2] == 1:  # Correct breed
                    results_stats['n_correct_breed'] += 1

            else:
                results_stats['n_notdogs_img'] += 1
                if results_dic[key][4] == 0:  # Correctly classified not-a-dog
                    results_stats['n_correct_notdogs'] += 1
        else:
            print(f"Warning: Entry {key} in results_dic has less than 4 elements.")

    # Calculer les pourcentages
    if results_stats['n_dogs_img'] > 0:
        results_stats['pct_correct_dogs'] = (results_stats['n_correct_dogs'] / results_stats['n_dogs_img']) * 100.0
        results_stats['pct_correct_breed'] = (results_stats['n_correct_breed'] / results_stats['n_dogs_img']) * 100.0
    else:
        results_stats['pct_correct_dogs'] = 0.0
        results_stats['pct_correct_breed'] = 0.0

    if results_stats['n_notdogs_img'] > 0:
        results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] / results_stats['n_notdogs_img']) * 100.0
    else:
        results_stats['pct_correct_notdogs'] = 0.0

    return results_stats
