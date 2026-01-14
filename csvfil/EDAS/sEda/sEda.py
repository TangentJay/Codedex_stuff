#9/23/2025
#Scuffed insta overview
#EDA stuff

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scuffed_Eda(csv_file):
    '''
    best pratice
    quick exploratory
    data analysis
    '''
    df = pd.read_csv(csv_file)

    print('View of teh data')
    print(df.head())
    
    print(f'shape: {df.shape}')
    
    print(f'\ncolumn info {(df.dtypes.value_counts())}')

    print('\nchecking for missing values')
    missingV = df.isnull().sum()
    print(missingV[missingV > 0] )


    print('\n numeric and categorie summary!')
    print('\n numeric')
    numV = df.select_dtypes(include=['number']).columns
    if len(numV) > 0:
        print(df[numV].describe())

    print('\n categorical')
    catV = df.select_dtypes(include=['object']).columns
    for col in catV[:3]: # 3 for output
        print(f'\n{col}: {df[col].nunique()} unique values')
        print(df[col].value_counts().head()) 

    print(' now we use some visualizations of teh data')
    #plots
    # fig, axes = plt.subplots(2,2, figsize=(15,8))
    fig, axes = plt.subplots(2,3, figsize=(15,8))  # 2 rows, 3 columns
    fig.patch.set_facecolor('lightgreen')

    sns.heatmap(df.isnull(), cbar=True, ax=axes[0,0])
    axes[0,0].set_title('Missing Values')

    
    #Scatter plot 
    if len(numV) >= 2:
        df.plot.scatter(x=numV[0], y=numV[1], ax=axes[0,2])
        axes[0,2].set_title(f'{numV[0]} vs {numV[1]}')
        axes[0,2].set_xlabel(numV[0])
        axes[0,2].set_ylabel(numV[1])
    elif len(numV) == 1 and len(catV) > 0:
   
        sns.boxplot(data=df, x=catV[0], y=numV[0], ax=axes[0,2])
        axes[0,2].set_title(f'{numV[0]} by {catV[0]}')

            #Add correlation 
    if len(numV) >= 2:
        correlation = df[numV[0]].corr(df[numV[1]])
        axes[1,2].text(0.5, 0.5, f'Correlation: {correlation:.3f}', 
                   transform=axes[1,2].transAxes, ha='center')
        axes[1,2].set_title('Correlation Info')



    #heatmap correlation
    if len(numV) > 1:
        sns.heatmap(df[numV].corr(), annot=True, ax=axes[0,1])
        axes[0,1].set_title('correlations')

    #histrogram distro
    if len(numV) > 0:
        df[numV[0]].hist(ax=axes[1,0])
        axes[1,0].set_title(f'Distributionz {numV[0]}')


    # trends over time
    date_cols = df.select_dtypes(include=['datetime']).columns
    if len(date_cols) > 0 and len(numV) > 0:
        df.plot(x=date_cols[0], y=numV[0], kind='line', ax=axes[2,1])
    #barz
    if len(catV) > 0:
        df[catV[0]].value_counts().head().plot(kind='bar', ax=axes[1,1])
        axes[1,1].set_title(f'Categoriez: {catV[0]}')

    


    plt.tight_layout()
    plt.show()


scuffed_Eda('mtl.csv')    