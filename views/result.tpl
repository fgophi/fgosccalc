<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="robots" content="noindex,nofollow,noarchive">
        <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css">
        <link rel="stylesheet" href="static/style.css">
        <link rel="canonical" href="/">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        <title>FGOスクショ差分チェッカー</title>
    </head>
    <body>
        <header class="row">
            <span class="logo">FGOスクショ差分チェッカー<small>(α version)</small></span>
        </header>
        % if result:
        <div class="row">
            <div class="card fluid">
                <h3 class="section">解析結果</h3>
                <p>{{ result }}</p>
                <p><pre>{{ formatted_output }}</pre></p>
                <p>
                    <a
                        class="twitter-share-button"
                        href="https://twitter.com/intent/tweet?text={{ quoted_output }}&url="
                        data-size="large">
                        Tweet
                    </a>
                </p>
                <table>
                    <thead>
                        <tr>
                            <th>ドロップ</th>
                            <th>差分</th>
                            <th>周回前</th>
                            <th>周回後</th>
                        </tr>
                    </thead>
                    % for pair in before_after_pairs:
                    <tr>
                        <td>{{ pair[0] }}</td>
                        <td data-label="差">{{ pair[3] }}</td>
                        <td data-label="前">{{ pair[1] }}</td>
                        <td data-label="後">{{ pair[2] }}</td>
                    </tr>
                    % end
                </table>
            </div>
        </div>
        <div class="row">
            <div class="card fluid">
                <div class="section">
                    % if before_im:
                    <img class="image" src="data:image/png;base64,{{ before_im }}">
                    % end
                    % if after_im:
                    <img class="image" src="data:image/png;base64,{{ after_im }}">
                    % end
                </div>
            </div>
        </div>
        <div class="row">
            <div class="card fluid">
            <h3 class="section"><a href="/items" target="_blank">未知アイテム一覧</a></h3>
            <p>
                解析結果に <code>item000001</code> のような名称不明アイテムが含まれている場合、それは未知のアイテムです。
                上記のリンク先で対応する画像を調べることができます。
            </p>
            </div>
        </div>
        % end
        <p><a href="/">戻る</a></p>
    </body>
</html>
