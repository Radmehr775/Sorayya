

fig = go.Figure(data=ohlcv)
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{'xaxis.range': [min(dates), max(dates)]}],
                    label='Reset',
                    method='relayout'
                ),
                dict(
                    args=[{'xaxis.range': [
                        max(dates) - timedelta(hours=1), max(dates) + timedelta(minutes=1)]}],
                    label='1h',
                    method='relayout'
                ),
                dict(
                    args=[{'xaxis.range': [
                        max(dates) - timedelta(days=1), max(dates) + timedelta(days=1)]}],
                    label='1d',
                    method='relayout'
                ),
                dict(
                    args=[{'xaxis.range': [
                        max(dates) - timedelta(weeks=1), max(dates) + timedelta(days=1)]}],
                    label='1w',
                    method='relayout'
                ),
                dict(
                    args=[{'xaxis.range': [
                        max(dates) - timedelta(days=30), max(dates) + timedelta(days=1)]}],
                    label='1m',
                    method='relayout'
                ),
                dict(
                    args=[{'xaxis.range': [
                        max(dates) - timedelta(days=365), max(dates) + timedelta(days=1)]}],
                    label='1y',
                    method='relayout'
                )
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.1,
            xanchor='left',
            y=1.1,
            yanchor='top'
        ),
    ]
)
fig.show()
