/**
 *  * wallet_check.js
  * ----------------
   * Real WDK (Wallet Development Kit) integration for Tether FanShield AI.
    *
     * This generates a real self-custodial wallet using Tether's WDK,
      * fetches its address, and checks its balance.
       *
        * Track: WDK (Wallets)
         */

         import WDK from '@tetherto/wdk';
         import WalletManagerEvm from '@tetherto/wdk-wallet-evm';

         async function main() {
           console.log('='.repeat(50));
             console.log('  TETHER FANSHIELD AI - Wallet Check (WDK)');
               console.log('='.repeat(50));

                 // 1. Generate a new self-custodial wallet
                   const seedPhrase = WDK.getRandomSeedPhrase();
                     console.log('\nGenerated new self-custodial wallet.');
                       console.log('(Seed phrase shown here ONLY for demo purposes -');
                         console.log(' in a real app, NEVER print or share this.)\n');

                           // 2. Initialize WDK and REGISTER the Ethereum wallet manager
                             const wdk = new WDK(seedPhrase)
                                 .registerWallet('ethereum', WalletManagerEvm, {
                                       provider: 'https://eth.drpc.org'
                                           });

                                             // 3. Get an Ethereum account from the wallet
                                               const account = await wdk.getAccount('ethereum', 0);
                                                 const address = await account.getAddress();
                                                   console.log('Wallet address:', address);

                                                     // 4. Check native ETH balance
                                                       try {
                                                           const balance = await account.getBalance();
                                                               console.log('ETH balance:', balance);
                                                                 } catch (err) {
                                                                     console.log('Balance check skipped:', err.message);
                                                                       }

                                                                         console.log('\n--- FanShield Safety Reminder ---');
                                                                           console.log('This is YOUR wallet. You hold the keys - not Tether,');
                                                                             console.log('not FanShield, not any exchange. Before sending USDT');
                                                                               console.log('to any "ticket seller" or "prize claim" address,');
                                                                                 console.log('run it through the FanShield scam scanner first.');
                                                                                 }

                                                                                 main().catch((err) => {
                                                                                   console.error('Error:', err.message);
                                                                                   });
                                                                                   
