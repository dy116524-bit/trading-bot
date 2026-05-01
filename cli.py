import typer
import logging
from rich.console import Console
from rich.table import Table
from bot.client import BinanceTestnetClient
from bot.orders import create_order_payload
import os

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("trading_bot.log"), logging.StreamHandler()]
)

app = typer.Typer()
console = Console()

@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading pair, e.g., BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET or LIMIT"),
    qty: float = typer.Option(..., help="Quantity to trade"),
    price: float = typer.Option(None, help="Price (required for LIMIT orders)")
):
    """Place an order on Binance Futures Testnet."""
    
    # Load credentials (use environment variables for security)
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        console.print("[bold red]Error:[/bold red] API credentials not found in environment variables.")
        raise typer.Exit()

    bot_client = BinanceTestnetClient(api_key, api_secret)

    try:
        payload = create_order_payload(symbol, side, order_type, qty, price)
        
        with console.status("[bold green]Placing order..."):
            response = bot_client.place_futures_order(**payload)

        # UI Response Table
        table = Table(title="Order Execution Summary")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("Order ID", str(response.get("orderId")))
        table.add_row("Status", response.get("status"))
        table.add_row("Executed Qty", response.get("executedQty"))
        table.add_row("Avg Price", response.get("avgPrice", "N/A"))
        
        console.print(table)
        console.print("[bold green]✔ Success![/bold green]")

    except Exception as e:
        console.print(f"[bold red]FAILED:[/bold red] {e}")

if __name__ == "__main__":
    app()
