# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
from bs4 import BeautifulSoup
# import re
import pandas as pd
# import numpy as np
# import csv
from urllib.request import Request, urlopen
from multiprocessing import Process, Manager, Pool
import time
from urllib.error import HTTPError



# 'id' , 'keywords' , 'genres' , 'original_title' , 'overview' , 'cast' , 'crew'
def scrape_2(ser, shared_data, counter):
    temp_list = []
    for title in ser:

        # setting up empty variables
        cast = ''
        genre = ''
        crew = ''
        keywords = ''
        overview = ''

        # Format the title to be put in search query
        title_form = title.strip().replace(' ','%20').replace('â€','-')
        site = f"https://www.imdb.com/find/?q={title_form}&ref_=nv_sr_sm"
        hdr1 = {'User-Agent': 'Mozilla/5.0'}
        req1 = Request(site,headers=hdr1)

        # Putting Error codes to handle Errors
        ERR1 = 'Page Timed out'
        ERR2 = 'Movie Link error'

        # OPEN PAGE TO EXTRACT SEARCH RESULTS
        # Try to open the page and handle Unicode error if page was not found
        try:
            page1 = urlopen(req1)
        except :
            # If no search results were found, put invalid results for entire row and continue on loop
            print(title_form,ERR1, '-- No Search results found')
            temp_list.append(['Invalid;ID', 'Invalid;Keywwords', 'Invalid;Genre', title_form , 'Invalid;Overview', 'Invalid;Cast', 'Invalid;Crew'])
            continue
        soup1 = BeautifulSoup(page1, 'html.parser')
        res = soup1.find_all('a', class_ = 'ipc-metadata-list-summary-item__t', role = 'button')


        # OPEN PAGE TO EXTRACT MOVIE_ID
        # Try to create a link from search result page, if no result was found, handle the error
        try:
            movie_link = f"https://www.imdb.com{res[0]['href']}"
        except IndexError:
            # If no movie ID was found, put invalid results for entire row and continue on loop
            print(title_form,ERR2, '-- Invalid IMDB ID')
            temp_list.append(['Invalid;ID', 'Invalid;Keywwords', 'Invalid;Genre', title_form , 'Invalid;Overview', 'Invalid;Cast', 'Invalid;Crew'])
            continue
        movie_id =  res[0]['href'].split('/')[2][2:]
        


        # OPEN MOVIE PAGE TO EXTRACT CAST AND GENRE
        # Try to open the page and handle Unicode error if page was not found
        req2 = Request(movie_link,headers=hdr1)
        try:
            page2 = urlopen(req2)
            soup2 = BeautifulSoup(page2, 'html.parser')
            a1_tags = soup2.find_all('a', attrs = {'data-testid':'title-cast-item__actor'})
            span_tags = soup2.find_all('span', attrs = {'class':'ipc-chip__text'})
        except :
            print(title_form,ERR1, '-- Invalid Cast and genre')
            cast = 'Invalid;Cast'
            genre = 'Invalid;Genre'


        # OPEN CREW PAGE TO EXTRACT CREW INFO
        crew_url = "https://www.imdb.com/title/tt"+movie_id+"/fullcredits/?ref_=tt_cl_sm"
        req3 = Request(crew_url,headers=hdr1)
        # Try to open the page and handle Unicode error if page was not found
        try:
            page3 = urlopen(req3)
            soup3 = BeautifulSoup(page3, 'html.parser')
            data = soup3.find_all('td', class_='name')
        except :
            print(title_form, ERR1, '--Invlid Crew info')
            crew = 'Invalid;Crew'
            
        
        # OPEN KEYWORDS PAGE FOR SPECIFIC MOVIE
        key_url = "https://www.imdb.com/title/tt"+movie_id+"/keywords/?ref_=tt_stry_kw"
        req4 = Request(key_url,headers=hdr1)
        # Try to open the page and handle Unicode error if page was not found
        try:
            page4 = urlopen(req4)
            soup4 = BeautifulSoup(page4, 'html.parser')
            key_data = soup4.find_all('a', class_='ipc-metadata-list-summary-item__t')
        except :
            print(title_form, ERR1, '--Invlid Keywords')
            keywords = 'Invalid;Keywords'
            
        

        # OPEN OVERVIEW PAGE FOR SPECIFIC MOVIE
        overview_url = "https://www.imdb.com/title/tt"+movie_id+"/plotsummary/?ref_=tt_stry_pl"
        req5 = Request(overview_url,headers=hdr1)
        # Try to open the page and handle Unicode error if page was not found
        try:
            page5 = urlopen(req5)
            soup5 = BeautifulSoup(page5, 'html.parser')
            overview_data = soup5.find_all('div', class_='ipc-html-content-inner-div')
        except :
            print(title_form, ERR1, '--Invlid Overview data')
            overview = 'Invalid;Overview'
            

        #After accessing all the webpage info, its time to collect data

        # Setting valid cast and genre
        if cast == '':
            for a in a1_tags:
                cast += a.text + ';'
        if genre == '':
            genre_list = []
            for spn in span_tags:
                genre_list += spn
            try:
                genre = ';'.join(genre_list[:-1])
            except TypeError:
                genre = 'Invalid;Genre'


        # Setting valid crew 
        if crew == '':
            for name in data:
                crew += str(name.text).strip()+';'
        

        # Setting valid keywords
        if keywords == '':
            for key in key_data:
                keywords += key.text+';'


        # Setting up overview data 
        if overview == '':
            try:
                overview = overview_data[2].text.replace(' ',';')
            except IndexError:
                overview = 'Invalid;Overview'

        temp_list.append([movie_id, keywords, genre, title_form, overview, cast, crew])
        counter.value += 1
        print(counter)

    shared_data.append(temp_list)


def main():
    start = time.time()
    mov_raw = pd.read_excel(r"C:\Users\aniru\OneDrive\Documents\SRC\SRC 4\All_movies_2013-2023.xlsx")
    title_series = pd.Series(mov_raw.loc[:,'TITLE'])
    test_titles1 = title_series[1500:2200]
    test_titles2 = title_series[2200:2900]
    test_titles3 = title_series[2900:3600]
    test_titles4 = title_series[3600:4300]
    test_titles5 = title_series[4300:]
    with Manager() as manager:
        shared_data = manager.list()
        counter = manager.Value('i',0)
        # arguments = [test_titles1]
        arguments = [test_titles1, test_titles2, test_titles3, test_titles4, test_titles5]
        processes = []
        for arg in arguments:
            process = Process(target=scrape_2, args=(arg, shared_data,counter))
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
        
        cols = ['id' , 'keywords' , 'genres' , 'original_title' , 'overview' , 'cast' , 'crew']
        final_df = pd.DataFrame(columns = cols)
        for data in list(shared_data):
            temp_df = pd.DataFrame(data, columns= cols)
            final_df = pd.concat([final_df, temp_df], ignore_index = True)
        end = time.time()
        final_df.to_csv('output-3.csv', index = False)
    total_time = end-start
    print(f"Total time taken = {total_time}") 

if __name__ == "__main__":
    main()
    


# def dummy(num, shared_data):
#     temp = []
#     for i in range(num):
#         temp.append([f"{num}",f"{num}",f"{num}",f"{num}",f"{num}",f"{num}",f"{num}",])
#     shared_data.append(temp)

# def main():
#     with Manager() as manager:
#         shared_data = manager.list()
#         arguments = [5,6,7,8,9]
#         processes = []
#         for arg in arguments:
#             process = Process(target = dummy, args = (arg, shared_data))
#             processes.append(process)
#             process.start()
#         for process in processes:
#             process.join()


#         final_df = pd.DataFrame(columns = ['a','b','c','d','e','f','g'])
#         # res = np.zeros((1,5))
#         for arr in list(shared_data):
#             temp_df = pd.DataFrame(arr, columns = ['a','b','c','d','e','f','g'])
#             final_df = pd.concat([final_df, temp_df], ignore_index = True)
#         print(type(final_df))
        

# if __name__ == '__main__':
#     main()

