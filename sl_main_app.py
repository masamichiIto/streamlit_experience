import streamlit as sl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib


def main():
    sl.title('GROUP BYとORDER BYをするwebアプリ')
    sl.header('GROUP BYとORDER BYをするwebアプリ')
    sl.markdown(
        """
        ここでは，GROUPBYとORDERBYをGUIでできるアプリケーションを作成する．  
        アイデアが思い浮かべば，随時他ページにアプリを追加していく．  
        """
        )
    sl.subheader('集計対象のデータのアップロード')
    datafile = sl.file_uploader('ここにCSVファイルをアップロードしてください(1ファイルのみ)', type=['csv'])
    if datafile is not None:
        df = pd.read_csv(datafile)

        sl.subheader('集計処理の指定')
        choice = sl.selectbox('実施する集計処理を選択してください．', ['集約+ソート', 'ソート'])
        check_obj = sl.selectbox(f'実施する処理は，{choice}でお間違えないでしょうか', ['No', 'Yes'])
        if check_obj == 'Yes':
            basis_cols = sl.multiselect(f'{choice}の基準となるカラム名を指定してください', options=df.columns)
            if choice == '集約+ソート':
                if len(basis_cols) > 0:
                    agg_cols = sl.multiselect('集約処理を施すカラム名を指定してください', options=set(df.columns)-set(basis_cols))
                    if len(agg_cols) > 0:
                        agg_dict = {}
                        for col in agg_cols:
                            agg_dict[col] = sl.selectbox(f'{col}　に対して実施する集約関数を選んでください', ['sum', 'count', 'mean', 'std', 'nunique'])
                        sl.json(agg_dict)
                        if sl.selectbox('上記で集約処理を実施しても良いでしょうか．', ['No', 'Yes']) == 'Yes':
                            sl.dataframe(df.groupby(by=basis_cols, as_index=False).agg(agg_dict))
            else:
                if sl.selectbox(f'並べ替えの基準カラムは{basis_cols}でお間違えないでしょうか', ['No', 'Yes']) == 'Yes':
                    sl.dataframe(df.sort_values(by=basis_cols, ascending=False))
        else:
            sl.write('集計処理を選び直して再度確認してください．')
    

    sl.subheader('データの可視化')
    if sl.checkbox('可視化は必要でしょうか？必要な場合はチェックボックスをチェックしてください'):
        ## 可視化の処理
        'まだ何も作ってないよーん！'


if __name__ == '__main__':
    main()