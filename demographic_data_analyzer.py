import pandas as pd

def demographic_analysis(file_path):
    # Veri setini oku
    df = pd.read_csv(file_path)

    # Her ırktan kaç kişi temsil ediliyor?
    race_counts = df['race'].value_counts()

    # Erkeklerin ortalama yaşı kaçtır?
    mean_age_male = df[df['sex'] == 'Male']['age'].mean()

    # Lisans diplomasına sahip kişilerin yüzdesi nedir?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # İleri düzeyde eğitim almış kişilerin yüzde kaçı 50.000'den fazla kazanıyor?
    advanced_degree_percentage = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')].shape[0] / df.shape[0] * 100

    # İleri eğitimi olmayan insanların yüzde kaçı 50 binden fazla kazanıyor?
    no_advanced_degree_percentage = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')].shape[0] / df.shape[0] * 100

    # Bir kişi haftada en az kaç saat çalışır?
    min_hours_per_week = df['hours-per-week'].min()

    # Haftada asgari saat çalışan kişilerin yüzde kaçının 50 binin üzerinde maaşı var?
    min_hours_per_week_salary_percentage = df[df['hours-per-week'] == min_hours_per_week]['salary'].value_counts(normalize=True)['>50K'] * 100

    # 50.000'den fazla kazanan insan yüzdesi en yüksek olan ülke hangisidir ve bu yüzde nedir?
    highest_earning_country_percentage = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True).max() * 100
    highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True).idxmax()

    # Hindistan'da 50 binden fazla kazananlar için en popüler mesleği belirleyin.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Sonuçları yuvarlayalım
    mean_age_male = round(mean_age_male)
    percentage_bachelors = round(percentage_bachelors)
    advanced_degree_percentage = round(advanced_degree_percentage)
    no_advanced_degree_percentage = round(no_advanced_degree_percentage)
    min_hours_per_week = round(min_hours_per_week)
    min_hours_per_week_salary_percentage = round(min_hours_per_week_salary_percentage)
    highest_earning_country_percentage = round(highest_earning_country_percentage)

    return {
        'race_counts': race_counts,
        'mean_age_male': mean_age_male,
        'percentage_bachelors': percentage_bachelors,
        'advanced_degree_percentage': advanced_degree_percentage,
        'no_advanced_degree_percentage': no_advanced_degree_percentage,
        'min_hours_per_week': min_hours_per_week,
        'min_hours_per_week_salary_percentage': min_hours_per_week_salary_percentage,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'highest_earning_country': highest_earning_country,
        'top_IN_occupation': top_IN_occupation
    }